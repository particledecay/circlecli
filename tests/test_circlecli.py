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
        results = self.circlecli.me(False)

        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.me()
        test results as json
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_me_as_json(self):

        results = self.circlecli.me(True)

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.projects()
        test results as a dict
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_projects_as_dict(self):
        results = self.circlecli.projects(False)
        print results
        
        self.assertEqual(results, ['therealbarack/circlecli'])

    """ CircleAPI.projects()
        test results as json
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_projects_as_json(self):

        results = self.circlecli.projects(True)
        print results

        data = json.loads(results)

        self.assertEqual(data[0]['branches']['master']['last_success']['status'], 'fixed')

    """ CircleAPI.builds()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_as_dict(self):
        results = self.circlecli.builds('therealbarack', 'circlecli', 1, False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.builds()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_as_json(self):

        results = self.circlecli.builds('therealbarack', 'circlecli', 1, True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.artifacts()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_artifacts_as_dict(self):
        results = self.circlecli.artifacts(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.artifacts()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_artifacts_as_json(self):

        results = self.circlecli.artifacts(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.retry_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_retry_build_as_dict(self):
        results = self.circlecli.retry_build(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.retry_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_retry_build_as_json(self):

        results = self.circlecli.retry_build(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.cancel_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_cancel_build_as_dict(self):
        results = self.circlecli.cancel_build(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.cancel_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_cancel_build_as_json(self):

        results = self.circlecli.cancel_build(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.ssh_users()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_ssh_users_as_dict(self):
        results = self.circlecli.ssh_users(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.ssh_users()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_ssh_users_as_json(self):

        results = self.circlecli.ssh_users(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.new_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_new_build_as_dict(self):
        results = self.circlecli.new_build(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.new_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_new_build_as_json(self):

        results = self.circlecli.new_build(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.create_ssh()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_ssh_as_dict(self):
        results = self.circlecli.create_ssh(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.create_ssh()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_ssh_as_json(self):

        results = self.circlecli.create_ssh(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.list_checkout_keys()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_list_checkout_keys_as_dict(self):
        results = self.circlecli.list_checkout_keys(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.list_checkout_keys()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_list_checkout_keys_as_json(self):

        results = self.circlecli.list_checkout_keys(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.create_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_checkout_key_as_dict(self):
        results = self.circlecli.create_checkout_key(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.create_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_checkout_key_as_json(self):

        results = self.circlecli.create_checkout_key(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_checkout_key_as_dict(self):
        results = self.circlecli.checkout_key(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_checkout_key_as_json(self):

        results = self.circlecli.checkout_key(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.delete_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_delete_checkout_key_as_dict(self):
        results = self.circlecli.delete_checkout_key(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.delete_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_delete_checkout_key_as_json(self):

        results = self.circlecli.delete_checkout_key(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.clear_cache()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_clear_cache_as_dict(self):
        results = self.circlecli.clear_cache(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.clear_cache()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_clear_cache_as_json(self):

        results = self.circlecli.clear_cache(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.add_circle_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_circle_key_as_dict(self):
        results = self.circlecli.add_circle_key(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.add_circle_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_circle_key_as_json(self):

        results = self.circlecli.add_circle_key(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.add_heroku_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_heroku_key_as_dict(self):
        results = self.circlecli.add_heroku_key(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.add_heroku_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_heroku_key_as_json(self):

        results = self.circlecli.add_heroku_key(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.envar()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_envar_as_dict(self):
        results = self.circlecli.envar(False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.envar()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_envar_as_json(self):

        results = self.circlecli.envar(True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

if __name__ == '__main__':
    unittest.main()
