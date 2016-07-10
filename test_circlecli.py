# -*- coding: utf-8 -*-

"""
Tests for the CircleCLI API library.

"""

import unittest

from httmock import with_httmock

import circlecli
import mocks.circlecli


class TestCircleCLI(unittest.TestCase):

    @with_httmock(mocks.circlecli.resource_get)
    def test_get_repository(self):
        owner = 'appneta'
        repo = 'burndown'

        results = circlecli.me(false)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('name' in results)
        self.assertEqual(results['name'], repo)

    @with_httmock(mocks.circlecli.resource_get)
    def test_get_user(self):
        user = 'danriti'

        results = circlecli.me(user)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('login' in results)
        self.assertEqual(results['login'], user)

if __name__ == '__main__':
    unittest.main()
