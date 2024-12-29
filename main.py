import kivy
kivy.require('2.3.1')

import kivymd

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel

from xkcd_api import get_comic

    
class XKCDLayout(BoxLayout):
    my_title = ObjectProperty()
    image_url = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_title()
        comic = get_comic()
        self.image_url = comic['img']
    
    def add_title(self):
        if not self.my_title:
            self.my_title = MDLabel()
        self.add_widget(self.my_title)

class XKCDApp(MDApp):
    def build(self):
        return XKCDLayout()
    

if __name__ == '__main__':
    XKCDApp().run()