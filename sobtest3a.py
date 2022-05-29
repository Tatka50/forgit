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
from kivy.uix.floatlayout import FloatLayout
import itertools


class Screen(BoxLayout):
  def __init__(self, **kwargs ):
        super(Screen, self).__init__(**kwargs)
        self.orientation = "vertical"
        cuvinte = " "
        box=BoxLayout()
        
        
        btn= Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn.bind(on_press=self.on_solution)
       
        box.add_widget(btn)
        self.my_output = Label(text_size= (None,None),
                          pos_hint={'center_x': 0.5, 'center_y': .95},
                          size_hint_y=None,
                          size = self.size,
                          height = self.size[1],
                          halign="center",
                          valign = "middle",)
        self.add_widget(self.my_output)
        self.add_widget(box)

        #self.my_output.bind(size=self.setting_function)
        #self.my_output.bind(size=self.setting_function)
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
       self.my_output.text = slovv
       i=i+1
       print(slov1)
       
class MyApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()
