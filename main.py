# class 1 to class10
# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout

# class Interpace(FloatLayout):
#     def hello(self):
#         print('Im from interpace')
# class MyApp(App):
#     def hello():
#         print('im from Myapp ')
# MyApp().run()


# # class113
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
 
# class Interpace(FloatLayout):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         btn=Button(text='Click me',size_hint=(0.3,0.1),pos_hint={'center_x':0.5,'center_y':0.5})
#         self.label=Label(text='Click me',size_hint=(0.3,0.1),pos_hint={'center_x':0.5,'center_y':0.6})
#         self.text=TextInput(text='Enter',size_hint=(0.3,0.1),pos_hint={'center_x':0.5,'center_y':0.7},multiline=True)
#         # self.text.bind(on_text_validate=self.button_press)

#         btn.bind(on_press=self.button_press) 
#         self.add_widget(self.text)
#         self.add_widget(self.label)
#         self.add_widget(btn)
        

#     def button_press(self,obj):
#         data=self.text.text
#         self.label.text=data  
# class MyApp(App):
#     def built(self):
#         return Interpace()
# MyApp().run()

# class 14

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Interpace(FloatLayout):
    def display(self):
        data=self.ids.textinput.text
        self.ids.label.text=data

class MyApp(App):
    pass
MyApp().run()

