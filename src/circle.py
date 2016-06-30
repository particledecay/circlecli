# -*- coding: utf-8 -*-
"""CLI wrapper for CircleCI's REST API."""
import requests
from urllib import urlencode
from urlparse import ParseResult, urlparse, urlunparse


class CircleAPI(object):
    """Simple wrapper for requests specific to CircleCI."""

    def __init__(self, token):
        """Load the API token.

        Args:
            token (str): the CircleCI API token (obtained at https://circleci.com/account/api)
        """
        self._token = token
        self._base_url = "https://circleci.com/api/v1"

    def build_url(self, endpoint, params={}):
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

    def get(self, endpoint, params={}, headers={}):
        """Request the URL at `endpoint`.

        Args:
            endpoint (str): the API endpoint after base URL
            params (dict): any params to include in the request

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        url = self.build_url(endpoint, params)
        new_headers = {'Content-Type': 'application/json'}
        new_headers.update(headers)

        r = requests.get(url, headers=new_headers)
        if r.status_code >= 400:
            raise Exception(u"Error sending GET request to {}".format(url))

        return r.json()

    def me(self):
        """Endpoint at /me.

        Returns:
            (dict) the JSON-converted response from the endpoint
        """
        return self.get('me')