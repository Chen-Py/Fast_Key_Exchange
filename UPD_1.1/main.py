from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
import configinit
from kivy.lang import Builder
from buttons import RoundedButton
from kivy.properties import ObjectProperty
from fkealgo import FKE

Builder.load_file('menuwindow.kv')

configinit.init()


algo = FKE()
sm = ScreenManager()

class GLayout(GridLayout):
    pass
class Page(Widget):
    pass
class BackButton(RoundedButton):
    def back(self):
        sm.current = "Menu"
    pass
class SubmitButton(RoundedButton):
    pass
class Menu_Page(Page):
    def move_to(self, name):
        sm.current = name
    pass

class Private_Page(Page): 
    input_N = ObjectProperty(None)
    input_m = ObjectProperty(None)
    input_p = ObjectProperty(None)
    result = ObjectProperty(None)
    def submit(self):
        if not self.input_N.text.isdigit() or not self.input_m.text.isdigit() or not self.input_p.text.isdigit() :
            self.result.text = "[color=ff0000]*INPUT INCORRECT*[/color]"
            return
        self.Private_Open_Code, self.Private_Secret_Code = algo.Make_Private_Code(int(self.input_N.text), int(self.input_m.text), int(self.input_p.text))
        self.result.text = 'Your Private Open Code (N, m, P) is:\n[color=ff0000]' + str(self.Private_Open_Code)+ '[/color]\nYour Private Secret Code (q) is:\n[color=ff0000]' + str(self.Private_Secret_Code) + '[/color]'
        pass
    pass

class Communication_Page(Page):
    input_N = ObjectProperty(None)
    input_m = ObjectProperty(None)
    input_P = ObjectProperty(None)
    input_q = ObjectProperty(None)
    def submit(self):
        if not self.input_N.text.isdigit() or not self.input_m.text.isdigit() or not self.input_P.text.isdigit() or not self.input_q.text.isdigit() :
            self.result.text = "[color=ff0000]*INPUT INCORRECT*[/color]"
            return
        self.Communication_Open_Code, self.Communication_Secret_Code, self.Key = algo.Make_Communication_Code(int(self.input_N.text), int(self.input_m.text), int(self.input_P.text), int(self.input_q.text))
        self.result.text = 'Your Communication Open Code (Q) is:\n[color=ff0000]' + str(self.Communication_Open_Code)+ '[/color]\nYour Communication Secret Code (q) is:\n[color=ff0000]' + str(self.Communication_Secret_Code) + "[/color]\n The Key (K) is:\n[color=ff0000]" + str(self.Key) + '[/color]'
    pass

class Key_Page(Page):
    input_Q = ObjectProperty(None)
    input_m = ObjectProperty(None)
    input_p = ObjectProperty(None)
    result = ObjectProperty(None)
    def submit(self):
        if not self.input_Q.text.isdigit() or not self.input_m.text.isdigit() or not self.input_p.text.isdigit():
            self.result.text = "[color=ff0000]*INPUT INCORRECT*[/color]"
            return
        self.Key = algo.Make_Key(int(self.input_Q.text), int(self.input_m.text), int(self.input_p.text))
        self.result.text = 'The Key is:\n[color=ff0000]' + str(self.Key) + '[/color]'
    pass

class FKEApp(App):
    def build(self):
        self.menu_page = Menu_Page()
        self.private_page = Private_Page()
        self.communication_page = Communication_Page()
        self.key_page = Key_Page()
        screen = Screen(name = 'Menu')
        screen.add_widget(self.menu_page)
        sm.add_widget(screen)
        screen = Screen(name = 'Make Private Code')
        screen.add_widget(self.private_page)
        sm.add_widget(screen)
        screen = Screen(name = 'Make Communication Code')
        screen.add_widget(self.communication_page)
        sm.add_widget(screen)
        screen = Screen(name = 'Make Key')
        screen.add_widget(self.key_page)
        sm.add_widget(screen)
        return sm

if __name__ == '__main__':
    app = FKEApp()
    app.run()