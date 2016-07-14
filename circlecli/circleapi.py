# -*- coding: utf-8 -*-
"""CLI wrapper for CircleCI's REST API."""
import json
import requests
from collections import OrderedDict
from dateutil import parser as dp, tz
from urllib import urlencode
from urlparse import ParseResult, urlparse, urlunparse


class CircleAPI(object):
    """Simple wrapper for requests specific to CircleCI."""

    def __init__(self, token):
        """Load the API token.

        Args:
            token (str): the CircleCI API token (obtained at https://circleci.com/account/api)
        """
        self._token = self._validate_token(token)
        self._base_url = "https://circleci.com/api/v1"

    def _validate_token(self, token):
        """Ensure the provided token is a valid CircleCI API token.

        Args:
            token (str): the CircleCI API token

        Returns:
            (str) a valid token
        """
        if len(token) != 40:
            raise ValueError(u"Invalid API token: {}".format(token))
        try:
            int(token, 16)
        except ValueError:
            raise ValueError(u"Invalid API token: {}".format(token))
        return token

    def _build_url(self, endpoint, params={}):
        """Return the full URL for the desired endpoint.

        Args:
            endpoint (str): the API endpoint after base URL
            params (dict): any params to include in the request

        Returns:
            (str) the full URL of the request
        """
        new_params = {'circle-token': self._token}
        new_params.update(params)

        parsed_url = urlparse(self._base_url)
        new_parse = ParseResult(scheme=parsed_url.scheme, netloc=parsed_url.netloc,
                                path='/'.join((parsed_url.path, endpoint)),
                                params='', query=urlencode(new_params),
                                fragment='')

        return urlunparse(new_parse)

    def _get(self, endpoint, params={}, headers={}):
        """Send a GET request to `endpoint`.

        Args:
            endpoint (str): the API endpoint after base URL
            params (dict): any params to include in the request
            headers (dict): any headers to include in the request

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        url = self._build_url(endpoint, params)
        new_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        new_headers.update(headers)

        r = requests.get(url, headers=new_headers)
        if r.status_code >= 400:
            raise Exception(u"Error sending GET request to {}".format(url))

        return r.json()

    def _post(self, endpoint, data=None, headers={}):
        """Send a POST request to `endpoint`.

        Args:
            endpoint (str): the API endpoint after base URL
            data (dict): the body to submit with the request
            headers (dict): any headers to include in the request

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        url = self._build_url(endpoint)
        new_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        new_headers.update(headers)

        r = requests.post(url, headers=new_headers, data=data)
        if r.status_code >= 400:
            raise Exception(u"Error sending POST request to {}".format(url))

        return r.json()

    def _delete(self, endpoint, headers={}):
        """Send a DELETE request to `endpoint`.

        Args:
            endpoint (str): the API endpoint after base URL
            headers (dict): any headers to include in the request

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        url = self._build_url(endpoint)
        new_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        new_headers.update(headers)

        r = requests.delete(url, headers=headers)
        if r.status_code >= 400:
            raise Exception(u"Error sending DELETE request to {}".format(url))

        return r.json()

    def _retr_item(self, obj, key):
        """Retrieve an item from a dict, including sub-keys.

        Args:
            obj (dict): a dict object
            key (str): a key to retrieve from `obj`

        Returns:
            () the item located at `key`
        """
        keys = key.split('.')
        item = obj
        for k in keys:
            if k not in item:
                raise KeyError
            item = item[k]
        return item

    def _filter_single(self, response, filters):
        """Filter a single response object by matching a provided set of filters.

        Args:
            response (dict): a response object
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) the response if it matches all filters
        """
        for k, v in filters.iteritems():
            try:
                item = self._retr_item(response, k)
            except KeyError:  # we know the key doesn't exist
                return
            try:
                # things like "true" need to be JSON-loaded to match a boolean
                if item != v and item != json.loads(v):
                    return
            except:
                return
        return response

    def _filter(self, response, filters={}):
        """Filter response by matching a provided set of filters.

        Args:
            filters (dict): a set of key/value pairs to match

        Returns:
            (list/dict) the original response filtered by the provided filters
        """
        if not filters:
            return response

        if isinstance(response, list):
            new_response = [r for r in response if self._filter_single(r, filters)]
        else:
            new_response = self._filter_single(response, filters)

        return new_response

    def me(self, verbose=False):
        """Provide information about the signed in user.

        Args:
            verbose (bool): whether to return filtered info or the full response

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        r_json = self._get('me')
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = OrderedDict()
        resp['Name'] = r_json['name']
        resp['Emails'] = ', '.join(r_json['all_emails'])
        resp['Sign-In Count'] = r_json['sign_in_count']
        resp['Heroku API Key'] = r_json['heroku_api_key']
        resp['Containers'] = r_json['containers']
        resp['Parallelism'] = r_json['parallelism']
        resp['Username'] = r_json['login']
        resp['Admin'] = r_json['admin']
        resp['Projects'] = ', '.join(r_json['projects'].keys())

        return resp

    def projects(self, verbose=False, filters={}):
        """List of all the projects you're following on CircleCI.

        Args:
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (list) a list of all the projects and project info
        """
        r_json = self._filter(self._get('projects'), filters)
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = ['{}/{}'.format(j['username'], j['reponame']) for j in r_json]
        return resp

    def builds(self, username=None, project=None, build_num=None, verbose=False,
               filters={}):
        """Last 30 build summaries for the account (or for a project).

        Args:
            username (str): the owner of the project
            project (str): the project name
            build_num (int): the build number
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (list) the last 30 build summaries
        """
        if username and project:
            if build_num:
                r_json = self._get('project/{username}/{project}/{build_num}'.format(**locals()))
            else:
                r_json = self._get('project/{username}/{project}'.format(**locals()))
        else:
            r_json = self._get('recent-builds')
        r_json = self._filter(r_json, filters)

        if verbose:
            return json.dumps(r_json, indent=2)

        resp = []
        if not isinstance(r_json, list):
            r_json = [r_json]
        for build in r_json:
            o = OrderedDict()
            o['Build# '] = build['build_num']
            o['Author '] = '{} <{}>'.format(build['author_name'], build['author_email']) if build['author_email'] else build['author_email']
            if build['vcs_tag']:
                o['Tag    '] = build['vcs_tag']
            else:
                o['Branch '] = build['branch'] or 'Unknown'
            dt = dp.parse(build.get('queued_at', build.get('usage_queued_at'))).astimezone(tz.tzlocal())
            o['Queued '] = dt.strftime('%a, %b %d, %Y %I:%M%p %Z')
            o['Trigger'] = build['why']
            o['URL    '] = build['build_url']
            o['Result '] = build['outcome']
            resp.insert(0, o)

        return resp

    def artifacts(self, username, project, build_num, verbose=False, filters={}):
        """List the artifacts produced by a given build.

        Args:
            username (str): the owner of the project
            project (str): the project name
            build_num (int): the build number
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (list) the artifacts produced by the build
        """
        r_json = self._filter(self._get('project/{username}/{project}/{build_num}/artifacts'.format(**locals())), filters)
        if verbose:
            return json.dumps(r_json, indent=2)
        return [ar['url'] for ar in r_json]

    def retry_build(self, username, project, build_num, verbose=False, filters={}):
        """Retry a given build.

        Args:
            username (str): the owner of the project
            project (str): the project name
            build_num (int): the build number
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) a summary of the new build
        """
        r_json = self._filter(self._post('project/{username}/{project}/{build_num}/retry'.format(**locals())), filters)
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = OrderedDict()
        resp['Build# '] = r_json['build_num']
        resp['Author '] = '{} <{}>'.format(r_json['author_name'], r_json['author_email']) if r_json['author_email'] else r_json['author_email']
        if r_json['vcs_tag']:
            resp['Tag    '] = r_json['vcs_tag']
        else:
            resp['Branch '] = r_json['branch'] or 'Unknown'
        dt = dp.parse(r_json.get('queued_at', r_json.get('usage_queued_at'))).astimezone(tz.tzlocal())
        resp['Queued '] = dt.strftime('%a, %b %d, %Y %I:%M%p %Z')
        resp['Trigger'] = r_json['why']
        resp['URL    '] = r_json['build_url']
        resp['Result '] = r_json['outcome']

        return resp

    def cancel_build(self, username, project, build_num, verbose=False, filters={}):
        """Cancel a given build.

        Args:
            username (str): the owner of the project
            project (str): the project name
            build_num (int): the build number
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) a summary of the canceled build
        """
        r_json = self._filter(self._post("project/{username}/{project}/{build_num}/cancel".format(**locals())), filters)
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = OrderedDict()
        resp['Build# '] = r_json['build_num']
        resp['Author '] = '{} <{}>'.format(r_json['author_name'], r_json['author_email']) if r_json['author_email'] else r_json['author_email']
        if r_json['vcs_tag']:
            resp['Tag    '] = r_json['vcs_tag']
        else:
            resp['Branch '] = r_json['branch'] or 'Unknown'
        dt = dp.parse(r_json.get('queued_at', r_json.get('usage_queued_at'))).astimezone(tz.tzlocal())
        resp['Queued '] = dt.strftime('%a, %b %d, %Y %I:%M%p %Z')
        resp['Trigger'] = r_json['why']
        resp['URL    '] = r_json['build_url']
        resp['Result '] = r_json['outcome']

        return resp

    def ssh_users(self, username, project, build_num, verbose=False, filters={}):
        """Add a user to the build's SSH permissions.

        Args:
            username (str): the owner of the project
            project (str): the project name
            build_num (int): the build number
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) confirmation of the added user
        """
        raise NotImplementedError(u"This method has not yet been implemented.")

    def new_build(self, username, project, branch="master", data=None, verbose=False,
                  filters={}):
        """Trigger a new build.

        Args:
            username (str): the owner of the project
            project (str): the project name
            branch (str): the branch to use for the build
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) a summary of the new build
        """
        r_json = self._filter(self._post("project/{username}/{project}/tree/{branch}".format(**locals()),
                                         data=data), filters)
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = OrderedDict()
        resp['Build# '] = r_json['build_num']
        resp['Author '] = '{} <{}>'.format(r_json['author_name'], r_json['author_email']) if r_json['author_email'] else r_json['author_email']
        if r_json['vcs_tag']:
            resp['Tag    '] = r_json['vcs_tag']
        else:
            resp['Branch '] = r_json['branch'] or 'Unknown'
        dt = dp.parse(r_json['queued_at']).astimezone(tz.tzlocal())
        resp['Queued '] = dt.strftime('%a, %b %d, %Y %I:%M%p %Z')
        resp['Trigger'] = r_json['why']
        resp['URL    '] = r_json['build_url']
        resp['Result '] = r_json['outcome']

        return resp

    def create_ssh(self, username, project, filters={}):
        """Create an SSH key used to access key-based external systems.

        Args:
            username (str): the owner of the project
            project (str): the project name
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) confirmation of the added key
        """
        raise NotImplementedError(u"This method has not yet been implemented.")

    def list_checkout_keys(self, username, project, filters={}):
        """List checkout keys.

        Args:
            username (str): the owner of the project
            project (str): the project name
            filters (dict): a set of key/value pairs to match

        Returns:
            (list) the checkout keys
        """
        return self._filter(self._get('project/{username}/{project}/checkout-key'.format(**locals())), filters)

    def create_checkout_key(self, username, project, filters={}):
        """List checkout keys.

        Args:
            username (str): the owner of the project
            project (str): the project name
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) confirmation of the added key
        """
        raise NotImplementedError(u"This method has not yet been implemented.")

    def checkout_key(self, username, project, fingerprint, filters={}):
        """Get a checkout key.

        Args:
            username (str): the owner of the project
            project (str): the project name
            fingerprint (str): the fingerprint of the checkout key
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) a single checkout key
        """
        return self._filter(self._get('project/{username}/{project}/checkout-key/{fingerprint}'.format(**locals())), filters)

    def delete_checkout_key(self, username, project, fingerprint, filters={}):
        """Delete a checkout key.

        Args:
            username (str): the owner of the project
            project (str): the project name
            fingerprint (str): the fingerprint of the checkout key
            filters (dict): a set of key/value pairs to match

        Returns:
            (dict) a single checkout key
        """
        return self._filter(self._delete('project/{username}/{project}/checkout-key/{fingerprint}'.format(**locals())), filters)

    def clear_cache(self, username, project, verbose=False):
        """Clear the cache for a project.

        Args:
            username (str): the owner of the project
            project (str): the project name
            verbose (bool): whether to return filtered info or the full response

        Returns:
            (dict) confirmation of the cleared cache
        """
        r_json = self._delete('project/{username}/{project}/build-cache'.format(**locals()))
        if verbose:
            return json.dumps(r_json, indent=2)

        resp = OrderedDict()
        resp['status'] = r_json['status']

        return resp

    def add_circle_key(self):
        """Add a CircleCI key to your GitHub user account.

        Returns:
            (dict) confirmation of the key addition
        """
        raise NotImplementedError(u"This method has not yet been implemented.")

    def add_heroku_key(self):
        """Add your Heroku API key to CircleCI.

        Returns:
            (dict) confirmation of the key addition
        """
        raise NotImplementedError(u"This method has not yet been implemented.")

    def envvar(self, username, project, verbose=False, filters={}, **envvars):
        """List or add environment variables for a project.

        Args:
            username (str): the owner of the project
            project (str): the project name
            verbose (bool): whether to return filtered info or the full response
            filters (dict): a set of key/value pairs to match
            **envvars (dict): variables to set

        Return:
            (dict/list) confirmation of the variable addition or list of variables
        """
        data = [{"name": k, "value": v} for k, v in envvars.iteritems()]

        resp = []
        if len(data) > 0:
            for d in data:
                r_json = self._post("project/{username}/{project}/envvar".format(**locals()),
                                    data=json.dumps(d))
                if r_json:
                    resp.append(r_json)
        else:
            r_json = self._filter(self._get("project/{username}/{project}/envvar".format(**locals())), filters)
            if r_json:
                resp.extend(r_json)

        if verbose:
            return json.dumps(resp, indent=2)

        formatted_resp = []
        for var in resp:
            formatted_resp.append("{}: {}".format(var['name'], var['value']))
        return formatted_resp