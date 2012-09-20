#!/usr/bin/env python
import sys

import os
from os.path import dirname, abspath

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoratings.tests.settings'

from django.test.simple import DjangoTestSuiteRunner


def runtests(*test_args):
    # parent = dirname(abspath(__file__))
    # sys.path.insert(0, parent)
    test_runner = DjangoTestSuiteRunner()
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
