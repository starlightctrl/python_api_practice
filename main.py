import kivy
kivy.require('2.3.1')

import kivymd

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel

    
class XKCDLayout(BoxLayout):
    my_title = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_title()
    
    def add_title(self):
        if not self.my_title:
            self.my_title = MDLabel()
        self.add_widget(self.my_title)

    # title = MDLabel(text="Random XKCD Viewer", halign="center")

class XKCDApp(MDApp):
    def build(self):
        return XKCDLayout()
    

if __name__ == '__main__':
    XKCDApp().run()