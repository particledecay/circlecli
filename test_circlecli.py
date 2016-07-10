# -*- coding: utf-8 -*-

"""
Tests for the CircleCLI API library.

"""

import json
import unittest

from httmock import with_httmock

from circlecli import CircleAPI
import mocks.circlecli


class TestCircleCLISetup(unittest.TestCase):
    
    """ CircleAPI.init() should check the token is a 40-digit hex string
        and return an error if it is not
    """
    def test_valid_token(self):
        circlecli = CircleAPI('moo')

    def test_invalid_token(self):
        circlecli = CircleAPI('foo')

class TestCircleCLI(unittest.TestCase):
    
    def setUp(self):
        self.circlecli = CircleAPI('bar')

    @with_httmock(mocks.circlecli.resource_get)
    def test_me_as_dict(self):
        results = self.circlecli.me(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    @with_httmock(mocks.circlecli.resource_get)
    def test_me_as_json(self):

        results = self.circlecli.me(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['Username'], 'therealbarack')

if __name__ == '__main__':
    unittest.main()
