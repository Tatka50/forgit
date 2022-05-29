from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import datetime
from bs4 import BeautifulSoup

import requests
import datetime
from bs4 import BeautifulSoup
from xml.dom import minidom
import json
import xml.etree.ElementTree as ET
class MainApp(App):
 
   textinput = TextInput(text='Hello world')
   def on_enter(instance, value):
      print('User pressed enter in', instance)

textinput = TextInput(text='Hello world', multiline=False)
textinput.bind(on_text_validate=on_enter)    
       
if __name__ == '__main__':
    app = MainApp()
    app.run()
        
