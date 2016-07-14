import os
import unittest

from circlecli.circleutils import InvalidSectionError, UnrecognizedSectionError, \
                                  validate_circle_yml


class TestValidConfigMachine(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
machine:
    timezone:
        America/Los_Angeles
    ruby:
        version: 1.9.3-p0-falcon
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigMachine(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
machine:
    timezone:
        America/Los_Angeles
    ruby:
        - rvm install 1.9.3
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigMachine(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
machine:
    timezone:
        America/Los_Angeles
    override:
        - rvm install 1.9.3
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigGeneral(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    artifacts:
        - foo/bar.txt
        - baz/qux.txt
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigGeneral(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    artifacts:
        foo: bar
        baz: qux
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigGeneral(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    webhooks:
        - url: https://example.com
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigDependencies(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
dependencies:
    pre:
        - pip install foo
    override:
        - npm install
    bundler:
        without: [production, osx]
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigDependencies(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
dependencies:
    override: foo
    pre:
        bundler install:
            foo: bar
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigDependencies(unittest.TestCase):
    def setUp(self):
        self.circle = open('mocks/circle.yml', 'w')
        config = """
dependencies:
    override:
        - npm install 1.4.0
    notify: foo
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        os.remove(self.circle.name)

    def test_valid_general(self):
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)