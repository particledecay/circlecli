#!/usr/bin/env python
from setuptools import setup
from os import path as op


def _read(filename):
    """Read a file and return its contents."""
    try:
        return open(op.join(op.abspath(op.dirname(__file__)), filename)).read()
    except IOError:
        return ''


req_path = 'requirements.txt'
install_requires = [ln for ln in _read(req_path).split('\n') if ln and not ln.startswith('#')]
print repr(install_requires)


setup(
    name='circlecli',
    version='1.2.8',
    url='https://github.com/TheRealJoeLinux/circlecli',
    description=_read('DESCRIPTION'),
    long_description=_read('README.md'),
    author='Joey Espinosa',
    author_email='jlouis.espinosa@gmail.com',
    license='MIT License',
    keywords=['circleci', 'cicd', 'rest', 'api', 'cli', 'command', 'command-line'],
    install_requires=install_requires,
    packages=['circlecli'],
    py_modules=['circlecli'],
    classfiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Utilities',
    ],
    scripts=['bin/circlecli'],
    use_2to3=True,
)
