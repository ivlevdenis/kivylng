# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.textinput import TextInput
try:
    from .ui import *
except Exception as e:
    from ui import *


class TestTextInput(TextInput):
    pass


class TestApp(App):

    def __init__(self):
        super(TestApp, self).__init__()

    def build(self):
        pass
