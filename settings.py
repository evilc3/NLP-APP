from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox 
from kivy.uix.widget import Widget
from kivy.graphics import Color,Rectangle
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup



class SettingsBox(GridLayout):

    def __init__(self,**kwargs):
        super(SettingsBox,self).__init__(**kwargs)

        self.settings_list  = []

        

        self.cols = 1

        self.dict_options = {'Tokenizer':['word','sent','None'],
                                'StopWords':['nltk','Extend','None'],
                                'Stemmer':['Port','SnowBall','ISR'],
                                'Vectorizer':['Count','TfiDf','None']}
        
        self.list_operations  = ['Tokenizer','Stemmer','StopWords','Lemmatization','Vectorizers']
        
        self.default_settings = ['word','nltk','Port','Count']


        for i in self.dict_options:
            box = BoxLayout()
            box.add_widget(Label(text = i))

            for j in self.dict_options[i]:
       
                box.add_widget(Label(text = j))
                
                self.checkbox = CheckBox(group = j)
                self.checkbox.bind(on_press = self.get_settings)
                if j in self.default_settings:
                    self.checkbox.active = True
                if j == 'None':
                   self.checkbox.disabled = True 
                box.add_widget(self.checkbox)


            self.add_widget(box)   

    def get_settings(self,instance):
        try:
            if instance.active:
                self.settings_list.append(instance.group)
            elif not instance.active:
                self.settings_list.remove(instance.group)
        except:print('error')

        finally:
                print(self.settings_list)        


    def setting(self):
        return self.settings_list            