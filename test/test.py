# -*- codding: utf-8 -*-

import os
import sys

try:
    import kivy
except ImportError as e:
    sys.exit(1)

from importlib import import_module

from kivy.lang import Builder

test_kv_filename = os.path.join(os.getcwd(), 'test', 'testapp', 'test.kv')
work_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testapp')
sys.path.append(work_dir)

import_module('main')

kv = Builder.load_file(test_kv_filename)


class Test:

    def test_path(self):
        assert 'path' in kv.ids
