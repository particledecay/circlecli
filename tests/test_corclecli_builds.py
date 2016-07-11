# -*- coding: utf-8 -*-

"""
Tests for the CircleCLI API library.

"""

import json
import unittest

from httmock import with_httmock

from circlecli import CircleAPI
import mocks.circlecli


class TestCircleCLIBuilds(unittest.TestCase):
    
    def setUp(self):
        self.circlecli = CircleAPI('bar')

    """ CircleAPI.builds()
        test results as dict
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_as_dict(self):
        results = self.circlecli.builds(verbose=False)
        print results
        
        self.assertEqual(results[0]['Result '], 'failed')

    """ CircleAPI.builds()
        test results as json
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_as_json(self):

        results = self.circlecli.builds(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data[0]['subject'], 'corrected name of builds with project')

    """ CircleAPI.builds()
        test results as dict with project        
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_with_project_as_dict(self):
        results = self.circlecli.builds('therealbarack', 'circlecli', 1, verbose=False)
        print results
        
        self.assertEqual(results[0]['Result '], 'no_tests')

    """ CircleAPI.builds()
        test results as json with project        
    """
    @with_httmock(mocks.circlecli.resource_get)
    def test_builds_with_project_as_json(self):

        results = self.circlecli.builds('therealbarack', 'circlecli', 1, verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['outcome'], 'no_tests')

    """ CircleAPI.artifacts()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_artifacts_as_dict(self):
        results = self.circlecli.artifacts(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.artifacts()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_artifacts_as_json(self):

        results = self.circlecli.artifacts(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.retry_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_retry_build_as_dict(self):
        results = self.circlecli.retry_build(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.retry_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_retry_build_as_json(self):

        results = self.circlecli.retry_build(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.cancel_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_cancel_build_as_dict(self):
        results = self.circlecli.cancel_build(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.cancel_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_cancel_build_as_json(self):

        results = self.circlecli.cancel_build(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

    """ CircleAPI.new_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_new_build_as_dict(self):
        results = self.circlecli.new_build(verbose=False)
        print results
        
        self.assertEqual(results['Username'], 'therealbarack')

    """ CircleAPI.new_build()
        
    """
    @with_httmock(mocks.circlecli.resource_get)
    @unittest.skip("test not written yet")
    def test_new_build_as_json(self):

        results = self.circlecli.new_build(verbose=True)
        print results

        data = json.loads(results)

        self.assertEqual(data['login'], 'therealbarack')

if __name__ == '__main__':
    unittest.main()
