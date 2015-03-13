# -*- coding: utf-8 -*-

import os
import sys

try:
    import kivy
except ImportError as e:
    sys.exit(1)


from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Window.size = (800, 600)


class InterfaceManager(BoxLayout):
    pass


class PreviewApp(App):

    stats = ObjectProperty(None)

    def __init__(self, filename):
        super(PreviewApp, self).__init__()
        self.filename = filename
        self.root = InterfaceManager()
        Clock.schedule_interval(self.update_ui, .5)

    def on_stats(self, instance, value):
        self.root.clear_widgets()
        self.root.add_widget(Builder.load_file(self.filename))

    def update_ui(self, dt):
        self.stats = os.stat(self.filename)

    def build(self):
        pass


if __name__ == '__main__':
    from importlib import import_module
    sys.path.append(sys.argv[2])
    sys.path.append(os.getcwd())
    if os.path.isfile(os.path.join(sys.argv[2], 'main.py')) or \
            os.path.isfile(os.path.join(os.getcwd(), 'main.py')):
        import_module('main')
    else:
        sys.exit(1)
    app = PreviewApp(sys.argv[1])
    app.run()
