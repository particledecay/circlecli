# -*- coding: utf-8 -*-

"""
Mocks for the CircleCLI API library tests.

"""


from httmock import response, urlmatch

NETLOC = r'(.*\.)?circleci\.com$'
HEADERS = {'content-type': 'application/json'}
GET = 'get'
DELETE = 'delete'

class Resource:
    """ A CircleCli resource.

    :param path: The file path to the resource.

    """

    def __init__(self, path):
        self.path = path

    def get(self):
        """ Perform a GET request on the resource.

        :rtype: str

        """
        with open(self.path, 'r') as f:
            content = f.read()
        return content


    def delete(self):
        """ Perform a GET request on the resource.

        :rtype: str

        """
        with open(self.path, 'r') as f:
            content = f.read()
        return content

@urlmatch(netloc=NETLOC, method=GET)
def resource_get(url, request):
    file_path = url.netloc + url.path
    try:
        content = Resource(file_path).get()
    except EnvironmentError:
        # catch any environment errors (i.e. file does not exist) and return a
        # 404.
        return response(404, {}, HEADERS, None, 5, request)
    return response(200, content, HEADERS, None, 5, request)

@urlmatch(netloc=NETLOC, method=DELETE)
def resource_delete(url, request):
    file_path = url.netloc + url.path
    try:
        content = Resource(file_path).delete()
    except EnvironmentError:
        # catch any environment errors (i.e. file does not exist) and return a
        # 404.
        return response(404, {}, HEADERS, None, 5, request)
    return response(200, content, HEADERS, None, 5, request)
