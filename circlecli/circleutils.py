# -*- coding: utf-8 -*-
"""Utils for CircleCI."""
import os.path as op
import yaml


class InvalidNameError(Exception):
    def __init__(self, message, *args, **kwargs):
        super(InvalidNameError, self).__init__(message, *args, **kwargs)


class UnrecognizedSectionError(Exception):
    def __init__(self, message, *args, **kwargs):
        super(UnrecognizedSectionError, self).__init__(message, *args, **kwargs)


class InvalidSectionError(Exception):
    def __init__(self, message, *args, **kwargs):
        super(InvalidSectionError, self).__init__(message, *args, **kwargs)


def _errant_items(items, allowed_items):
    """Determine if any items are not allowed.

    Args:
        items (list): items to evaluate
        allowed_items (list): the only allowed items

    Returns:
        (set) unique errant values in `items`
    """
    if not isinstance(allowed_items, set):
        allowed_items = set(allowed_items)
    if not isinstance(items, set):
        items = set(items)

    return items.difference(allowed_items)


def validate_circle_yml(filepath):
    """Ensure a valid circle.yml according to CircleCI docs.

    Args:
        filepath (str): path to the circle.yml file

    Returns:
        (bool) True if a valid circle.yml
    """
    # obviously the file must be named 'circle.yml'
    if op.basename(filepath) != 'circle.yml':
        raise InvalidNameError(u"Filename must be 'circle.yml'")

    allowed_sections = {'checkout', 'database', 'dependencies', 'deployment',
                        'experimental', 'general', 'machine', 'test'}
    fd = open(filepath, 'r')  # let it raise an IOError if no file exists
    circle_yml = yaml.load(fd)  # will throw a ScannerError if not valid YaML
    circle_sections = circle_yml.keys()

    # check for valid sections
    unrecognized_sections = _errant_items(circle_sections, allowed_sections)
    if len(unrecognized_sections) > 0:
        # we have an unrecognized section
        raise UnrecognizedSectionError(u"The following sections are unrecognized: {}".format(", ".join(unrecognized_sections)))

    # check each section
    for section in circle_sections:
        if section == 'machine':
            conditions = {'pre', 'post'}  # override not allowed
            languages = {'ghc', 'java', 'node', 'php', 'python', 'ruby', 'xcode'}
            system = {'environment', 'hosts', 'services', 'timezone'}
            allowed = conditions.union(languages).union(system)
            subsections = circle_yml[section].keys()

            # check for valid subsections
            invalid_sections = _errant_items(subsections, allowed)
            if len(invalid_sections) > 0:
                # we have an invalid section
                raise InvalidSectionError(u"Sections not allowed in '{}': {}".format(section, ", ".join(invalid_sections)))

            # check each subsection
            for subsection in subsections:
                item = circle_yml[section][subsection]
                if subsection in ('environment', 'hosts'):  # dict requirement
                    if not isinstance(item, dict):
                        raise InvalidSectionError(u"'{}' not a valid item for '{}' section (must be 'ENV: VAR' format)".format(repr(item), subsection))
                elif subsection == 'timezone':  # string requirement
                    if not isinstance(item, basestring):
                        raise InvalidSectionError(u"'{}' section must be a single string".format(subsection))
                elif subsection == 'services':  # list requirement
                    if not isinstance(item, list):
                        raise InvalidSectionError(u"'{}' section must be a list".format(subsection))
                elif subsection in languages:
                    if not isinstance(item, dict) or len(item.keys()) != 1 or not item.get('version'):
                        raise InvalidSectionError(u"'{}' section only supports 'version'".format(subsection))
        elif section == 'checkout':
            allowed = {'post'}
            subsections = circle_yml[section].keys()

            # check for valid subsections
            invalid_sections = _errant_items(subsections, allowed)
            if len(invalid_sections) > 0:
                # we have an invalid section
                raise InvalidSectionError(u"Sections not allowed in '{}': {}".format(section, ", ".join(invalid_sections)))

            # check the only subsection
            item = circle_yml[section]['post']
            if not isinstance(item, list):
                raise InvalidSectionError(u"'{}' section must be a list".format('post'))
        elif section == 'dependencies':
            conditions = {'pre', 'override', 'post'}
            languages = {'bundler'}
            allowed = conditions.union(languages)
            subsections = circle_yml[section].keys()

            # check for valid subsections
            invalid_sections = _errant_items(subsections, allowed)
            if len(invalid_sections) > 0:
                # we have an invalid section
                raise InvalidSectionError(u"Sections not allowed in '{}': {}".format(section, ", ".join(invalid_sections)))

            # check each subsection
            for subsection in subsections:
                item = circle_yml[section][subsection]
                if subsection in conditions:
                    if not isinstance(item, list):
                        raise InvalidSectionError(u"'{}' section must be a list".format(subsection))
                else:
                    if not isinstance(item, dict):
                        raise InvalidSectionError(u"'{}.{}' subitem only supports 'without'".format(section, subsection))
                    allowed_subitems = {'without'}
                    subitems = circle_yml[section][subsection].keys()

                    # check for valid subitems
                    invalid_subitems = _errant_items(subitems, allowed_subitems)
                    if len(invalid_subitems) > 0:
                        # we have an invalid section
                        raise InvalidSectionError(u"Subitems not allowed in '{}.{}': {}".format(section, subsection, ", ".join(invalid_subitems)))

                    subsubitem = circle_yml[section][subsection]['without']
                    if not isinstance(subsubitem, list):
                        raise InvalidSectionError(u"'{}.{}' subitem must be a list".format(section, 'without'))

    return True
