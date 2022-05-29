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
    
    def btn_pressed(self,instance):
       
        button_text = instance.text 
        
        
    def build(self):
        box=BoxLayout() 
      
        txt_input = TextInput()  
        container_input = BoxLayout(orientation='horizontal', size_hint=[1, .1])
        container_input.add_widget(txt_input)
      
        btn_input = Button(text="Отправить", size_hint=[.5, 1])
        #btn_input.bind(on_press=lambda *a: MessageBox(txt_input.text, alias))
        container_input.add_widget(btn_input)
        
        
        box.add_widget(container_input)
        btn_input.bind(on_press=self.on_solution)
        
        return box
    def on_text(instance, value):
         print('The widget', instance, 'have:', value)

         textinput = TextInput()
         textinput.bind(text=on_text)
    textinput = TextInput(focus=True)
    def on_focus(instance, value):
       if value:
          print('User focused', instance)
       else:
          print('User defocused', instance)

    textinput = TextInput()
    textinput.bind(focus=on_focus)
    def on_solution(self, instance):
       
       url6="https://api.rasp.yandex.net/v3.0/search/?apikey=622f978d-a274-41bd-b297-e7de99a7ab1f&format=json&from=s9603877&to=s2006004&lang=ru_RU&page=1&date=2022-05-24"
     
       response = requests.get(url6.strip())
       data = response.json()
       slov1=[]
       i=0
        
       for item in data['segments']:
            it=item
            it=item['departure']
            slov1.append(it[11:16])
       #text_input.bind(focus=slov1)
       textinput = TextInput()
       textinput.bind(slov1)
    
       
if __name__ == '__main__':
    app = MainApp()
    app.run()
        
