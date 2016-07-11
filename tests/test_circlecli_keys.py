# -*- coding: utf-8 -*-

"""
Tests for the CircleCLI API library.

"""

import json
import unittest

from httmock import with_httmock

from circlecli import CircleAPI
import mocks.circlecli


class TestCircleCLIKeys(unittest.TestCase):
    
    def setUp(self):
        self.circlecli = CircleAPI('bar')

    """ CircleAPI.ssh_users()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_ssh_users_as_dict(self):
        results = self.circlecli.ssh_users(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.ssh_users()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_ssh_users_as_json(self):

        results = self.circlecli.ssh_users(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.create_ssh()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_ssh_as_dict(self):
        results = self.circlecli.create_ssh(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.create_ssh()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_ssh_as_json(self):

        results = self.circlecli.create_ssh(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.list_checkout_keys()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_list_checkout_keys_as_dict(self):
        results = self.circlecli.list_checkout_keys(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.list_checkout_keys()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_list_checkout_keys_as_json(self):

        results = self.circlecli.list_checkout_keys(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.create_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_checkout_key_as_dict(self):
        results = self.circlecli.create_checkout_key(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.create_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_create_checkout_key_as_json(self):

        results = self.circlecli.create_checkout_key(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_checkout_key_as_dict(self):
        results = self.circlecli.checkout_key(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_checkout_key_as_json(self):

        results = self.circlecli.checkout_key(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.delete_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_delete_checkout_key_as_dict(self):
        results = self.circlecli.delete_checkout_key(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.delete_checkout_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_delete_checkout_key_as_json(self):

        results = self.circlecli.delete_checkout_key(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.add_circle_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_circle_key_as_dict(self):
        results = self.circlecli.add_circle_key(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.add_circle_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_circle_key_as_json(self):

        results = self.circlecli.add_circle_key(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.add_heroku_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_heroku_key_as_dict(self):
        results = self.circlecli.add_heroku_key(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.add_heroku_key()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_add_heroku_key_as_json(self):

        results = self.circlecli.add_heroku_key(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

if __name__ == '__main__':
    unittest.main()
