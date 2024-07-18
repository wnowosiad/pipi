# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.lew_button = Button(text="Lew")
        self.lew_button.bind(on_press=self.show_lew)
        self.add_widget(self.lew_button)
        
        self.kot_button = Button(text="Kot")
        self.kot_button.bind(on_press=self.show_kot)
        self.add_widget(self.kot_button)
        
        self.pies_button = Button(text="Pies")
        self.pies_button.bind(on_press=self.show_pies)
        self.add_widget(self.pies_button)
        
        self.description_label = Label(text="Wybierz zwierzę z menu.")
        self.add_widget(self.description_label)

    def show_lew(self, instance):
        self.description_label.text = "Lew to duży drapieżnik z rodziny kotowatych, znany jako król zwierząt."

    def show_kot(self, instance):
        self.description_label.text = "Kot domowy to małe, mięsożerne ssaki, które są popularnymi zwierzętami domowymi."

    def show_pies(self, instance):
        self.description_label.text = "Pies to udomowiony ssak z rodziny psowatych, często nazywany najlepszym przyjacielem człowieka."

class AnimalApp(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    AnimalApp().run()