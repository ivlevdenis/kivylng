# -*- coding: utf-8

from kivy.uix.label import Label


class TestLabel(Label):

    def __init__(self, *args, **kwargs):
        super(TestLabel, self).__init__(*args, **kwargs)
        self.text = 'This TestLabel'
