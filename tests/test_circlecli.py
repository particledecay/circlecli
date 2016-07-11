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

    """ CircleAPI.me()
        test results as a dict
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_me_as_dict(self):
        results = self.circlecli.me(verbose=False)

        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.me()
        test results as json
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_me_as_json(self):

        results = self.circlecli.me(verbose=True)

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.projects()
        test results as a dict
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_projects_as_dict(self):
        results = self.circlecli.projects(verbose=False)

        self.assertEqual(results, ['therealbarack/circlecli'])

    """ CircleAPI.projects()
        test results as json
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_projects_as_json(self):

        results = self.circlecli.projects(verbose=True)

        data = json.loads(results)

        self.assertEqual(data[0]['branches']['master']['last_success']['status'], 'fixed')

    """ CircleAPI.clear_cache()
        
    """
    @with_httmock(mocks.circlecli.resource_delete)
    def test_clear_cache_as_dict(self):
        results = self.circlecli.clear_cache('therealbarack', 'circlecli', verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.clear_cache()
        
    """
    @with_httmock(mocks.circlecli.resource_delete)
    def test_clear_cache_as_json(self):

        results = self.circlecli.clear_cache('therealbarack', 'circlecli', verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.envar()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_envar_as_dict(self):
        results = self.circlecli.envar(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.envar()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_envar_as_json(self):

        results = self.circlecli.envar(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

if __name__ == '__main__':
    unittest.main()
