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
from settings import SettingsBox

from nlp_base import nlp

class DemoScreen(Screen):

    def __init__(self,**kwargs):
        super(DemoScreen,self).__init__(**kwargs)
        

        #object of nlp_base

        self.nlp_obj = nlp() 

         
        self.setting_layout2 = SettingsBox()
       
    
        #demo screen
        self.r = BoxLayout(pos_hint = {'x':0,'top':0.9})
        self.r.orientation = 'vertical'

        string = 'Add text here and experiment with the different settings to observe the output'

        self.input = TextInput(text = string,size_hint = (1,0.5))
        
        self.output  = TextInput(text = 'OUTPUT:',multiline  = True,disabled = True,size_hint = (1,0.5))
         
        # self.output.bind(size =self.)
        self.r.add_widget(self.input)
        

        
        
        
        self.list_operations  = ['Tokenizer','Stemmer','StopWords','Lemmatization','Vectorizers']
        
        self.dict_options = {'Tokenizer':['word','sent','None'],
                                'StopWords':['nltk','Extend','None'],
                                'Stemmer':['Port','SnowBall','ISR'],
                                'Vectorizer':['Count','TfiDf','None']}

        
        sgrid = BoxLayout()
        sgrid.orientation = 'vertical'
        sgrid.add_widget(self.setting_layout2)
        self.set = Button(text = 'SET',size_hint  = (1,0.2))
        self.set.bind(on_press = self.change_settings)
        sgrid.add_widget(self.set)    


        self.pop_setting = Popup(title = 'preprocessing Settings',content = sgrid, size_hint = (0.7,0.7))
        
        self.settings  = Button(text= 'CHANGE SETTINGS',size_hint = (0.8,0.1),pos_hint = {'center_x':0.5,'top':1,'center_y':0.5})
        self.settings.bind(on_press = self.show_settings)
        


        self.r.add_widget(self.settings)

        grid = GridLayout(size_hint = (0.9,0.5))
        grid.cols = 1

      


        self.checkbox_list = [CheckBox(group = self.list_operations[0]),CheckBox(group = self.list_operations[1]),
                                CheckBox(group = self.list_operations[2]),CheckBox(group = self.list_operations[3]),CheckBox(group = self.list_operations[4])]


        self.label_list = {self.list_operations[0]:Label(text = 'OFF'),
                           self.list_operations[1]:Label(text = 'OFF'),
                           self.list_operations[2]:Label(text = 'OFF'),
                           self.list_operations[3]:Label(text = 'OFF'),
                           self.list_operations[4]:Label(text = 'OFF')}
       
         
        for j,i in enumerate(self.list_operations):
            
     
                
            box = BoxLayout()
            box.add_widget(Label(text = i))
            box.add_widget(self.label_list[i])
            
         
            self.checkbox_list[j].bind(on_press = self.checker)
            box.add_widget(self.checkbox_list[j])
       
            
            grid.add_widget(box)
        
        self.r.add_widget(grid)
        

        # self.apply = Button(text = 'APPLY') 
        # self.apply.bind(on_press = self.checker)  
       
        # self.r.add_widget(self.apply)         
        self.r.add_widget(self.output)
        self.add_widget(self.r)

    def show_settings(self,instance):
        self.pop_setting.open()        


    def checker(self,instance):

            if instance.active:

                self.label_list[instance.group].text = 'ON'
                self.operations(type = instance.group ,active = 'ON')
            elif not instance.active:
                self.label_list[instance.group].text = 'OFF'
                self.operations(type = instance.group ,active = 'OFF')


    def change_settings(self,instance):
        self.pop_setting.dismiss()
        self.settings_list = self.setting_layout2.setting()
        # self.error_text .text = 'final settings:' + str(self.settings_list)
        print('final settings:',self.settings_list)
        
        if len(self.settings_list) > 0:
            for i in self.settings_list:
                self.nlp_obj.apply_settings(i)            



    def operations(self,type,active):
        # print('action applied:',type,'active',active)
        
        if type == self.list_operations[0] and active == 'ON':
            self.tmp  = self.input.text
            self.output.text = self.nlp_obj.get_tokens(input = self.tmp)
            # print(self.input.text)
        elif type == self.list_operations[0] and active == 'OFF':
            self.output.text = self.tmp  


        if type == self.list_operations[1] and active == 'ON':
            self.tmp  = self.input.text
            
            self.output.text = self.nlp_obj.get_stemmer(input = self.tmp)     
        elif type == self.list_operations[1] and active == 'OFF':
            self.output.text = self.tmp   




        if type == self.list_operations[2] and active == 'ON':
            self.tmp  = self.input.text
            
            
           

           

            self.output.text = self.nlp_obj.get_stopwords(input = self.tmp)
            # print(self.input.text)
        elif type == self.list_operations[2] and active == 'OFF':
            self.output.text = self.tmp       





        if type == self.list_operations[3] and active == 'ON':
            self.tmp  = self.input.text

            self.output.text = self.nlp_obj.lemmatize_sent(text = self.tmp)
        elif type == self.list_operations[3] and active == 'OFF':
            self.output.text = self.tmp   


        if type == self.list_operations[4] and active == 'ON':
            self.tmp  = self.input.text
            
            self.output.text = self.nlp_obj.get_vec(input = self.tmp)
        elif type == self.list_operations[4] and active == 'OFF':
            self.output.text = self.tmp       


    def select_options(self,instance,x):
        print(x)
        # setattr(instance,'text',x) 

        self.nlp_obj.apply_settings(x)


    def get_nlp(self):
        return self.nlp_obj    

