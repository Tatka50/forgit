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
    def __init__(self):
        super().__init__()
        self.label=Label(text='моя программа\nВсе работает')
      
    def btn_pressed(self,instance):
       
        button_text = instance.text 
        
        
    def build(self):
        box=BoxLayout()
        #btn=Button(text='vvv')
        #btn.bind(on_press=self.btn_pressed)
        #main_layout = BoxLayout(orientation="vertical")
        
        #main_layout.add_widget(self.solution)


        
        #btn.bind(on_press=self.on_button_press)
        
        btn= Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn.bind(on_press=self.on_solution)
       
        box.add_widget(self.label)
       
        box.add_widget(btn)
     
        return box             
  
    def on_solution(self, instance):
        #text = self.solution.text
    #if text:
        #solution = str(eval(self.solution.text))
        
      
       
       url6="https://api.rasp.yandex.net/v3.0/search/?apikey=622f978d-a274-41bd-b297-e7de99a7ab1f&format=json&from=s9603877&to=s2006004&lang=ru_RU&page=1&date=2022-05-24"
     
       response = requests.get(url6.strip())
       data = response.json()
       slov1=[]
       slovv=''
       slovvv=''
       i=0
       #for item in data:
           #print(item)     
       for item in data['segments']:
            it=item
            it=item['departure']
            slov1.append(it[11:16])
       while i!=len(slov1):
           slovv=slovv+slov1[i]
          
           i=i+1
       print(slovv)    
       self.label.text = slovv
       i=i+1
       print(slov1)
       
if __name__ == '__main__':
    app = MainApp()
    app.run()
        
