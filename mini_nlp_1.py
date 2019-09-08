
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
from kivy.uix.filechooser import FileChooserIconView



import time
import threading
import pandas as pd
import os

from demo_screen import DemoScreen
from settings import SettingsBox

        
class MainScreen2(Screen):

    def __init__(self,**kwargs):
        super(MainScreen2,self).__init__(**kwargs)
        layout = BoxLayout(pos_hint = {'top':0.9},size_hint=( 1,0.9))
        layout.orientation = 'vertical'

        self.setting_layout = SettingsBox()

        self.settings_list = []
        self.LABEL = 'None'
        
        self.col_list = []
       
        #layour for popup_precessing

        self.probox = BoxLayout()

        self.probox.orientation = 'vertical'

        self.nlp = DemoScreen().get_nlp()

        self.list = self.nlp.get_settings()
        
        
        self.probox.add_widget(Label(text= 'settings'))
        self.tokenizer = Label(text= 'Tokenizer selected : '+ self.list[0])
        self.probox.add_widget(self.tokenizer)
        
        self.stopwords = Label(text= 'Stop Words selected: '+ self.list[1])
        self.probox.add_widget(self.stopwords)
        
        self.stemmer = Label(text= 'Stemmer: '+ self.list[3])
        self.probox.add_widget(self.stemmer)


        self.vectorizer = Label(text= 'Vectorizer: ' +self.list[2]) 
        self.probox.add_widget(self.vectorizer)


        self.settings  = Button(text= 'CHANGE SETTINGS')
        self.settings.bind(on_press = self.show_settings)
        self.probox.add_widget(self.settings)
        self.button  = Button(text= 'Start Processing')
        self.button.bind(on_press = self.start_preprocessing)
        self.probox.add_widget(self.button)
        
        #end  of layout

        self.pop_precessing = Popup(title = 'preprocessing Settings',content = self.probox, size_hint = (0.5,0.5))
        
        
        sgrid = BoxLayout()
        sgrid.orientation = 'vertical'
        sgrid.add_widget(self.setting_layout)
        self.set = Button(text = 'SET',size_hint  = (1,0.2))
        self.set.bind(on_press = self.change_settings)
        sgrid.add_widget(self.set)    


        self.pop_setting = Popup(title = 'Change Settings',content = sgrid, size_hint = (0.7,0.7))
        





        #export file layout


        expbox = BoxLayout()
        expbox.orientation = 'vertical'

        self.file_name = TextInput(text = 'Enter File name',multiline = False)
        expbox.add_widget(self.file_name)
        self.exportb =  Button(text = 'EXPORT')
        self.exportb.bind(on_press = self.export)
        self.vecbutton = Button(text = 'Export Vectorizer Files')
        self.vecbutton.bind(on_press = self.vec)
        
        
        expbox.add_widget(self.exportb)
        expbox.add_widget(self.vecbutton)
        
        #end of layout


        
        
        self.pop_export = Popup(title = 'Export Settings',content = expbox, size_hint = (0.5,0.3))


        #main layout 
        #   

        vbox = BoxLayout(size_hint = (1,0.2),pos_hint = { 'top':1})
        vbox.orientation = 'vertical'

        hbox2 = BoxLayout(size_hint = (1,0.1))
        
        self.path = TextInput(pos_hint = { 'top':1},multiline = False)

        # self.path.text = r'C:\Users\CLIVE\Desktop\Project\machinehack hackthons\Participants_Data_News_category\Data_Train.xlsx'    
         

        hbox2.add_widget(TextInput(text = 'PATH::',size_hint = (0.1,1),disabled = True))
        hbox2.add_widget(self.path)



        hbox = BoxLayout(size_hint = (1,0.1),pos_hint = {'top':1})
        self.label = TextInput(text = 'None',pos_hint = {'top':1}) 
        self.encoding = TextInput(text = 'UTF-8',pos_hint = {'top':1})
        hbox.add_widget(TextInput(text = 'LABEL::',size_hint = (0.3,1),disabled = True))
        hbox.add_widget(self.label)
        hbox.add_widget(TextInput(text = 'ENCODING:',size_hint = (0.3,1),disabled = True))
        hbox.add_widget(self.encoding)



        
        self.importb = Button(text = 'import',size_hint = (1,0.1),pos_hint = { 'top':1})
        self.importb.bind(on_press = self.load_dataset)
        
        vbox.add_widget(hbox2)
        vbox.add_widget(hbox)
        vbox.add_widget(self.importb)
        
        layout.add_widget(vbox)  
       
      
        
        self.description  =  TextInput(text = 'Discription',size_hint = (1,0.2))
        layout.add_widget(self.description)     

        
       
        
       

        self.grid = GridLayout(size_hint = (1,0.3),pos_hint = {'top':1})
        self.grid.cols  = 3
        for i in range(6):
            self.grid.add_widget(Label(text = str(i)))
            self.grid.add_widget(Label(text = 'Keep'))
            self.grid.add_widget(CheckBox())


        layout.add_widget(self.grid)    
        
        self.pro_button = Button(text = 'preprocessing',size_hint = (1,0.1),pos_hint = {'top':1})
        self.pro_button.bind(on_press = self.popup_procesing)
        layout.add_widget(self.pro_button)

        self.button2 = Button(text = 'Export',size_hint = (1,0.1),pos_hint = {'top':1})
        self.button2.bind(on_press = self.popup_export)
        layout.add_widget(self.button2) 

        self.error_text = TextInput(text = 'Errors : 0 ',size_hint = (1,0.1)) 
        layout.add_widget(self.error_text)
       





        self.add_widget(layout)

    def get_settings(self,instance):
        
        try:
            if instance.active:
                self.settings_list.append(instance.group)
            elif not instance.active:
                self.settings_list.remove(instance.group)
        except:print('error')

        finally:
                print(self.settings_list)
             

    def change_settings(self,instance):
        self.pop_setting.dismiss()
        self.settings_list = self.setting_layout.setting()
        self.error_text .text = 'final settings:' + str(self.settings_list)
        print('final settings:',self.settings_list)
        
        if len(self.settings_list) > 0:
            for i in self.settings_list:
                self.nlp.apply_settings(i)


        list2 = self.nlp.get_settings()
        print('list2',list2)
        self.tokenizer.text = 'Tokenizer selected: '+list2[0]
        self.stopwords.text = 'StopWords selected: '+list2[1]
        self.stemmer.text = 'Stemmer selected: '+list2[3]
        self.vectorizer.text = 'Vectorizer selected: '+list2[2]

   
    def show_settings(self,instance):
        self.pop_setting.open()    

    def popup_procesing(self,instance):

        
        self.pop_precessing.open()    

    def popup_export(self,instance):
    
        
        self.pop_export.open()        


    def load_dataset(self,instance):

    
        try:    
            if self.encoding.text == '':
                self.encoding.text = 'UTF8'
                print(self.encoding.text)

            if self.pro_button.disabled:
                self.pro_button.disabled = False
                self.button2.disabled = False


            self.error_text.text = 'Importing please wait...'
            self.ext = self.path.text.split('.')[-1]
            print(self.ext)
            if self.ext == 'xlsx':
                print(self.path.text)
                self.dataset = pd.read_excel(io = self.path.text,encoding = self.encoding.text)
            elif self.ext == 'csv':
                print(self.encoding.text)
                self.dataset = pd.read_csv(self.path.text,encoding = self.encoding.text)
            elif self.ext == 'json':
                self.dataset  = pd.read_json(self.path.text,encoding= self.encoding.text)    
            else:
                self.error_text =  'file type not supported try .xlsx , .csv or .json'
                self.pro_button.disabled  = True 
                self.button2.disabled = True       
             

             

        
            #1 get null rows and cols if any 
            #2 get no. of rows and cols  size of dataset
            #3 different labels 
            self.LABEL = self.label.text

            self.columns = [i for i in self.dataset.columns.tolist() if i not in [self.LABEL]]

            print(self.columns)




            self.label_info = ' '
            # self.data_info = str(self.dataset.info())
            # print('******** info {} ********'.format(self.dataset.info()))
            if self.LABEL != 'None':
                self.label_info =str( self.dataset[self.LABEL].value_counts())
            

            self.description.text =  'total no. of records'+ str(len(self.dataset) )+ '\n' + 'COlumns Present ' + str(self.columns) + '\n' + self.label_info


            self.grid.clear_widgets()

        

            
            self.checkbox_list = []

            for i in self.columns:
                self.checkbox_list.append(CheckBox(group = i))   


            for j,i in enumerate(self.columns):

                self.grid.add_widget(Label(text = i))
                self.grid.add_widget(Label(text = 'Keep'))
                self.checkbox_list[j].bind(on_press = self.checker)
                self.grid.add_widget(self.checkbox_list[j])

        except Exception:
            print(Exception)
            self.error_text.text = 'Import error'
            self.description.text = 'file not found.... :/ or decoding error '
            self.pro_button.disabled  = True 
            self.button2.disabled = True   

    def checker(self,instance):
          if instance.active:

              self.col_list.append(instance.group)
              print('active')
    
          elif not instance.active:
              print('dactive')
              self.col_list.remove(instance.group)


          self.error_text.text = 'Selected Column for processing' + str(self.col_list)

    def start_preprocessing(self,instacne):

        self.pop_precessing.dismiss()
        self.error_text.text  = 'processing started please wait..'+ ' following actions will be applied '+ str(self.nlp.get_settings())
        self.pro_button.text = 'processing please wait....'
        
        threading.Thread(target=self.nlp_process).start()
        

    def nlp_process(self):
        self.pro_button.disabled  = True
        self.button2.disabled = True
        self.importb.disabled = True
        self.cols  = {}
        # print(self.text_data.text.split(' '))
        print(self.col_list[0])
        for i in self.col_list: 
            self.cols[i] = self.dataset[i].apply(self.nlp.nlp_cleaner) 
            # print(type(self.cols))
            # print(type(self.cols[i]))
            print(type(self.cols[i].values))
        # print(self.cols)
        print('total no. of cols',self.cols.keys())
        self.pro_button.disabled  = False
        self.button2.disabled = False
        self.importb.disabled = False

        self.pro_button.text = 'Processing'
        self.error_text.text = 'processing complete'

        # try:
        #     # self.thread._delete()
        # except:print('thread error')
            
    def export(self,instance):
        try:
            self.dataframe = pd.DataFrame(data = self.cols)
         
            if self.LABEL != 'None':
                self.export_data = pd.merge(self.dataframe,self.dataset[self.LABEL],on = self.dataset[self.LABEL].index)
                self.export_data.drop(columns = ['key_0'],inplace = True)

                self.save_file(data = self.export_data,path = self.file_name.text)            

                # self.export_data.to_excel(self.file_name.text)
                # self.error_text.text = 'file saved to path :' + os.getcwd() + '\\' + self.file_name.text
                

            else:
                self.save_file(data = self.dataframe,path = self.file_name.text)            
                # dataframe.to_excel(self.file_name.text)
                # self.error_text.text = 'file saved (without label) to path :' + os.getcwd() + '\\' + self.file_name.text
                
    
            # self.pop_export.dismiss()    
        except  Exception: 
                print('saving error')
                self.error_text.text = 'Saving Error make sure the file extension is either csv or xlsx'

    def save_file(self,data,path):
        ext = path.split('.')[-1]
        print('path entered is ::',path)

        try:
            if ext == 'csv':
                data.to_csv(path)
                self.error_text.text = 'file saved to path :' + os.getcwd() + '\\' + path 
            elif ext == 'xlsx':
                data.to_excel(path)
                self.error_text.text = 'file saved to path :' + os.getcwd() + '\\' + path 
            else: 
                self.error_text.text = 'file could not be saved . file extension should be .csv for .xlsx'

            
        except: self.error_text.text = 'invalid fileextension'
        
    def vec(self,instance):

        try: 
            
        # print(self.dataframe[self.col_list[0]])
            self.nlp.create_vec(col= self.col_list[0],name = self.file_name.text,encoding = self.encoding.text)
            self.error_text.text +=self.error_text.text + '\n' + 'Vectorizer and vectorized metrix saved in :'+os.getcwd()    

        except: self.error_text.text = 'export error: make sure dataset is imported and preprocessed'


        
class MyGrid(RelativeLayout):


    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)


        

        


        # self.demo = Button(text = 'DEMO',size_hint = (0.2,0.1),pos_hint = {'x':0.3,'top':1})
        # self.main = Button(text = 'MAIN',size_hint = (0.2,0.1),pos_hint = {'x':0.5,'top':1})
        
        self.demo = ToggleButton(text = 'Setting',group = 'type',size_hint = (0.2,0.1),pos_hint = {'x':0.5,'top':1})
        self.main = ToggleButton(text = 'Main',group = 'type',state = 'down',size_hint = (0.2,0.1),pos_hint = {'x':0.3,'top':1})


        self.sm = ScreenManager()


        self.main_screen = MainScreen2(name = 'Main')
        self.demo_screen = DemoScreen(name = 'Setting')
         
        self.sm.add_widget(self.main_screen) 
        self.sm.add_widget(self.demo_screen)
        


        self.layout  = RelativeLayout(size_hint = (1,1))


        self.layout.add_widget(self.sm)
        
        self.demo.bind(on_press = self.change_state)
        self.main.bind(on_press = self.change_state)

     
        self.add_widget(self.main)
        self.add_widget(self.demo)
        self.add_widget(self.layout)

    def change_state(self,instance):
        
      
        self.sm.current =   instance.text

      

        


        


        





        
        
        

        



class TutorialApp(App):

    def build(self):

        
        return  MyGrid()


   


if __name__ == "__main__":
    a = TutorialApp()    
    a.run()


