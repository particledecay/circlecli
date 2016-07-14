import os
import unittest

from circlecli.circleutils import InvalidSectionError, UnrecognizedSectionError, \
    validate_circle_yml


class TestValidConfigMachine(unittest.TestCase):
    """Test a valid config for the Machine section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
machine:
    pre:
        - curl -k -L -o phantomjs.tar.bz2 http://phantomjs.googlecode.com/files/phantomjs-1.8.2-linux-x86_64.tar.bz2
        - tar -jxf phantomjs.tar.bz2
    environment:
        foo: bar
        baz: 123
    hosts:
        dev.circleci.com: 127.0.0.1
        foobar: 1.2.3.4
    timezone:
        America/Los_Angeles
    java:
        version: openjdk7
    node:
        version: 0.11.8
    ruby:
        version: 1.9.3-p0-falcon
    php:
        version: 5.4.5
    python:
        version: 2.7.5
    ghc:
        version: 7.8.3
    services:
        - redis
        - elasticsearch
        - neo4j
        - cassandra
        - riak
        - docker
        - memcached
        - rabbitmq-server
        - beanstalkd
        - couchbase-server
        - sphinxsearch
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigMachine(unittest.TestCase):
    """Test an unaccepted format for the Machine section."""

    def setUp(self):
        """Create a mock circle.yml file."""
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
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigMachine(unittest.TestCase):
    """Test an unrecognized subsection for the Machine section."""

    def setUp(self):
        """Create a mock circle.yml file."""
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
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigCheckout(unittest.TestCase):
    """Test a valid config for the Checkout section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
checkout:
    post:
        - git submodule sync
        - git submodule update --init
        - mv config/.app.yml config/app.yml
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigCheckout(unittest.TestCase):
    """Test an unaccepted format for the Machine section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
checkout:
    post:
        foo: bar
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigCheckout(unittest.TestCase):
    """Test an unrecognized subsection for the Machine section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
checkout:
    pre:
        - git submodule sync
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigDependencies(unittest.TestCase):
    """Test a valid config for the Dependencies section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
dependencies:
    pre:
        - gem uninstall bundler
        - gem install bundler --pre
    override:
        - npm install
    post:
        - pip install -r requirements.txt
    bundler:
        without: [production, osx]
    cache_directories:
        - "assets/cache"
        - "~/assets/output"
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigDependencies(unittest.TestCase):
    """Test an unaccepted format for the Dependencies section."""

    def setUp(self):
        """Create a mock circle.yml file."""
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
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigDependencies(unittest.TestCase):
    """Test an unrecognized subsection for the Dependencies section."""

    def setUp(self):
        """Create a mock circle.yml file."""
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
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigDatabase(unittest.TestCase):
    """Test a valid config for the Database section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
database:
    pre:
        - wget -O dump.sql https://foo.us-east-a.s3.amazonaws.com/dump.sql
    override:
        - mysql -u ubuntu circle_test < dump.sql
    post:
        - bundle exec rake db:create db:schema:load --trace
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigDatabase(unittest.TestCase):
    """Test an unaccepted format for the Database section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
database:
    pre:
        foo: bar
    override:
        - mysql -u ubuntu circle_test < dump.sql
    post:
        - bundle exec rake db:create db:schema:load --trace
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigDatabase(unittest.TestCase):
    """Test an unrecognized subsection for the Database section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
database:
    pre:
        foo: bar
    override:
        - mysql -u ubuntu circle_test < dump.sql
    without:
        - bundle exec rake db:create db:schema:load --trace
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigTest(unittest.TestCase):
    """Test a valid config for the Test section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
test:
    pre:
        - pip install nose2==0.6.5
    override:
        - phpunit my/special/subdirectory/tests
    post:
        - bundle exec rake spinach:
            environment:
                RAILS_ENV: test
    minitest_globs:
        - test/integration/**/*.rb
        - test/extra-dir/**/*.rb
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigTest(unittest.TestCase):
    """Test an unaccepted format for the Test section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
test:
    pre:
        - pip install nose2==0.6.5
    override:
        - phpunit my/special/subdirectory/tests
    post:
        - bundle exec rake spinach:
            environment:
                RAILS_ENV: test
    minitest_globs:
        first_dir: test/integration/**/*.rb
        second_dir: test/extra-dir/**/*.rb
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigTest(unittest.TestCase):
    """Test an unrecognized subsection for the Test section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
test:
    pre:
        - pip install nose2==0.6.5
    override:
        - phpunit my/special/subdirectory/tests
    post:
        - bundle exec rake spinach:
            environment:
                RAILS_ENV: test
    bundler:
        first_dir: test/integration/**/*.rb
        second_dir: test/extra-dir/**/*.rb
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigDeployment(unittest.TestCase):
    """Test a valid config for the Deployment section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
deployment:
    production:
        branch: production
        commands:
            - ./deploy_prod.sh
    automerge:
        branch: [dev_alice, dev_bob, dev_carol]
        commands:
            - ./merge_to_master.sh
    feature:
        branch: /feature_.*/
        commands:
            - ./deploy_feature.sh
    master:
        branch: master
        owner: circleci
        commands:
            - ./deploy_master.sh
    release:
        tag: /v[0-9]+(\.[0-9]+)*/
        owner: circleci
        heroku:
            appname: h-circleci-prod
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigDeployment(unittest.TestCase):
    """Test an unaccepted format for the Deployment section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
deployment:
    production:
        branch: production
        commands: foo
    automerge:
        branch: [dev_alice, dev_bob, dev_carol]
        commands:
            - ./merge_to_master.sh
    feature:
        branch: /feature_.*/
        commands:
            - ./deploy_feature.sh
    master:
        branch: master
        owner: circleci
        commands:
            - ./deploy_master.sh
    release:
        tag: /v[0-9]+(\.[0-9]+)*/
        owner: circleci
        commands:
            - ./deploy_master.sh
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigDeployment(unittest.TestCase):
    """Test an unrecognized subsection for the Deployment section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
deployment:
    pre:
        - ./gcloud-auth.sh
    production:
        branch: production
        commands:
            - ./deploy_prod.sh
    automerge:
        branch: [dev_alice, dev_bob, dev_carol]
        commands:
            - ./merge_to_master.sh
    feature:
        branch: /feature_.*/
        commands:
            - ./deploy_feature.sh
    master:
        branch: master
        owner: circleci
        commands:
            - ./deploy_master.sh
    release:
        tag: /v[0-9]+(\.[0-9]+)*/
        owner: circleci
        commands:
            - ./deploy_master.sh
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestMissingBranchConfigDeployment(unittest.TestCase):
    """Test a missing required subsection in Deployment section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
deployment:
    production:
        branch: production
        commands:
            - ./deploy_prod.sh
    automerge:
        branch: [dev_alice, dev_bob, dev_carol]
        commands:
            - ./merge_to_master.sh
    feature:
        branch: /feature_.*/
        commands:
            - ./deploy_feature.sh
    master:
        owner: circleci
        commands:
            - ./deploy_master.sh
    release:
        tag: /v[0-9]+(\.[0-9]+)*/
        owner: circleci
        commands:
            - ./deploy_master.sh
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigNotify(unittest.TestCase):
    """Test a valid config for the Notify section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
notify:
    webhooks:
        - url: https://example.com/hooks/circle
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigNotify(unittest.TestCase):
    """Test an unaccepted format for the Notify section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
notify:
    webhooks:
        url: https://example.com/hooks/circle
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigNotify(unittest.TestCase):
    """Test an unrecognized subsection for the Notify section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
notify:
    pre:
        - sudo apt-get install growl
    webhooks:
        - url: https://example.com/hooks/circle
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigGeneral(unittest.TestCase):
    """Test a valid config for the General section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    branches:
        ignore:
            - gh-pages
            - /release\/.*/
    build_dir: api
    artifacts:
        - "selenium/screenshots"
        - "~/simplecov"
        - "test.txt"
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigGeneral(unittest.TestCase):
    """Test an unaccepted format for the General section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    branches:
        - gh-pages
        - /release\/.*/
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigGeneral(unittest.TestCase):
    """Test an unrecognized subsection for the General section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
general:
    branches:
        ignore:
            - gh-pages
            - /release\/.*/
    build_dir: api
    artifacts:
        - "selenium/screenshots"
        - "~/simplecov"
        - "test.txt"
    post:
        - mkdir $CIRCLE_ARTIFACTS/json_output
        - mv solo/target/*.json $CIRCLE_ARTIFACTS/json_output
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)


class TestValidConfigExperimental(unittest.TestCase):
    """Test a valid config for the Experimental section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
experimental:
    notify:
        branches:
            only:
                - /feature.*/
            ignore:
                - /feature\.experiment.*/
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_valid_config(self):
        """Should detect a valid config."""
        self.assertTrue(validate_circle_yml(self.circle.name))


class TestInvalidConfigExperimental(unittest.TestCase):
    """Test an unaccepted format for the Experimental section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
experimental:
    notify:
        branches:
            only: /feature.*/
            ignore: /feature\.experiment.*/
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(InvalidSectionError, validate_circle_yml, self.circle.name)


class TestUnrecognizedConfigExperimental(unittest.TestCase):
    """Test an unrecognized subsection for the Experimental section."""

    def setUp(self):
        """Create a mock circle.yml file."""
        self.circle = open('mocks/circle.yml', 'w')
        config = """
experimental:
    notify:
        webhooks:
            - url: https://example.com/hooks/circleci
        branches:
            only:
                - /feature.*/
            ignore:
                - /feature\.experiment.*/
        """
        self.circle.write(config)
        self.circle.close()

    def tearDown(self):
        """Remove the mock circle.yml file."""
        os.remove(self.circle.name)

    def test_invalid_config(self):
        """Should detect an invalid config."""
        self.assertRaises(UnrecognizedSectionError, validate_circle_yml, self.circle.name)