import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
import configinit
configinit.init()
class FKE:
	def pow(self,n,a,mod):
		if(a==0):
			return 1
		if(a%2==1):
			return (n*pow(n,a-1,mod))%mod
		if(a%2==0):
			temp=pow(n,a/2,mod)
			return (temp*temp)%mod

	def Make_Private_Code(self,N,m,p):
		P=pow(N,p,m)
		self.Private_Open_Code=(N,m,P)
		self.Private_Secret_Code=p
		return (self.Private_Open_Code,self.Private_Secret_Code)

	def Make_Communication_Code(self,N,m,P,q):
		Q=pow(N,q,m)
		K=pow(P,q,m)
		self.Communication_Open_Code=Q
		self.Communication_Secret_Code=q
		self.Key=K
		return (Q,q,K)

	def Make_Key(self,Q,m,p):
		self.Key=pow(Q,p,m)
		return self.Key

algo=FKE()

class menu_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1
		self.add_widget(Label(text="M E N U",halign="center",valign="middle",height=Window.size[0]*0.1,size_hint_y=None,font_size=30))
		
		self.Make_Priate_Code_Button=Button(text="Make Pravate Code",halign="center",valign="middle",font_size=30)
		self.Make_Priate_Code_Button.bind(on_press=self.make_private_code_button)
		self.add_widget(self.Make_Priate_Code_Button)

		self.Make_communication_Code_Button=Button(text="Make Communication Code",halign="center",valign="middle",font_size=30)
		self.Make_communication_Code_Button.bind(on_press=self.make_communication_code_button)
		self.add_widget(self.Make_communication_Code_Button)


		self.Make_Key_Button=Button(text="Make Key",halign="center",valign="middle",font_size=30)
		self.Make_Key_Button.bind(on_press=self.make_key_button)
		self.add_widget(self.Make_Key_Button)

	def make_private_code_button(self,instance):
		MyApp.make_private_code_page.output.text="Your Private Code will be here ~"
		MyApp.screen_manager.current="Make_Priate_Code"

	def make_communication_code_button(self,instance):
		MyApp.make_communication_code_page.output.text="The Communication Code will be here ~"
		MyApp.screen_manager.current="Make_Communication_Code"

	def make_key_button(self,instance):
		MyApp.make_key_page.output.text="The Key will be here ~"
		MyApp.screen_manager.current="Make_Key"

class back_button(Button):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.text="Back To Menu"
		self.height=Window.size[0]*0.06
		self.size_hint_y=None
		self.font_size=20
		self.bind(on_press=self.back_to_menu)

	def back_to_menu(self,instance):
		MyApp.screen_manager.current="Menu"

class make_private_code_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1
		self.add_widget(Label(text="Make Private Code",halign="center",valign="middle",height=Window.size[0]*0.1,size_hint_y=None,font_size=30))
		

		self.input_tittle=GridLayout(height=Window.size[0]*0.06,size_hint_y=None)
		self.input_tittle.cols=4
		self.input_tittle.rols=1
		self.input_tittle.add_widget(Label(text="",font_size=20))
		self.input_tittle.add_widget(Label(text="N",font_size=20))
		self.input_tittle.add_widget(Label(text="m",font_size=20))
		self.input_tittle.add_widget(Label(text="p",font_size=20))

		self.add_widget(self.input_tittle)

		self.input_Nmp=GridLayout(height=Window.size[0]*0.1,size_hint_y=None)
		self.input_Nmp.cols=4
		self.input_Nmp.rols=1
		self.input_Nmp.add_widget(Label(text="Please input\nN m and p"))
		self.input_N=TextInput()
		self.input_m=TextInput()
		self.input_p=TextInput()
		self.input_Nmp.add_widget(self.input_N)
		self.input_Nmp.add_widget(self.input_m)
		self.input_Nmp.add_widget(self.input_p)

		self.add_widget(self.input_Nmp)



		self.submit_button=Button(text="Submit",height=Window.size[0]*0.06,size_hint_y=None,font_size=20)
		self.submit_button.bind(on_press=self.submit)

		self.add_widget(self.submit_button)

		self.output=Label(text="Your Private Code will be here ~",font_size=20)
		self.add_widget(self.output)

		
		self.add_widget(back_button())

	def submit(self,instance):
		if not self.input_N.text.isdigit() or not self.input_m.text.isdigit() or not self.input_p.text.isdigit() :
			self.output.text="Stupid Guy ! ! !   Check Your Input ! ! !"
			return
		algo.Make_Private_Code(int(self.input_N.text),int(self.input_m.text),int(self.input_p.text))
		self.output.text="Your Private Open Code is:\n"+str(algo.Private_Open_Code)+"\nYour Private Secret Code is:\n"+str(algo.Private_Secret_Code)
		self.output.halign="center"
		self.output.valign="middle"
		

class make_communication_code_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1
		self.add_widget(Label(text="Make Communication Code",halign="center",valign="middle",height=Window.size[0]*0.1,size_hint_y=None,font_size=30))


		self.input_tittle=GridLayout(height=Window.size[0]*0.06,size_hint_y=None)
		self.input_tittle.cols=5
		self.input_tittle.rols=1
		self.input_tittle.add_widget(Label(text="",font_size=20))
		self.input_tittle.add_widget(Label(text="N",font_size=20))
		self.input_tittle.add_widget(Label(text="m",font_size=20))
		self.input_tittle.add_widget(Label(text="P",font_size=20))
		self.input_tittle.add_widget(Label(text="q",font_size=20))



		self.add_widget(self.input_tittle)

		self.input_NmPq=GridLayout(height=Window.size[0]*0.1,size_hint_y=None)
		self.input_NmPq.cols=5
		self.input_NmPq.rols=1
		self.input_NmPq.add_widget(Label(text="Please input\nN m P and q"))
		self.input_N=TextInput()
		self.input_m=TextInput()
		self.input_P=TextInput()
		self.input_q=TextInput()
		self.input_NmPq.add_widget(self.input_N)
		self.input_NmPq.add_widget(self.input_m)
		self.input_NmPq.add_widget(self.input_P)
		self.input_NmPq.add_widget(self.input_q)


		self.add_widget(self.input_NmPq)

		self.submit_button=Button(text="Submit",height=Window.size[0]*0.06,size_hint_y=None,font_size=20)
		self.submit_button.bind(on_press=self.submit)

		self.add_widget(self.submit_button)

		self.output=Label(text="The Communication Code will be here ~",font_size=20)
		self.add_widget(self.output)

		self.add_widget(back_button())

	def submit(self,instance):
		if not self.input_N.text.isdigit() or not self.input_m.text.isdigit() or not self.input_P.text.isdigit() or not self.input_q.text.isdigit() :
			self.output.text="Stupid Guy ! ! !   Check Your Input ! ! !"
			return
		algo.Make_Communication_Code(int(self.input_N.text),int(self.input_m.text),int(self.input_P.text),int(self.input_q.text))
		self.output.text="The Communication Open Code is:\n"+str(algo.Communication_Open_Code)+"\nThe Communication Secret Code is:\n"+str(algo.Communication_Secret_Code)+"\nThe Key is:\n"+str(algo.Key)
		self.output.halign="center"
		self.output.valign="middle"

class make_key_page(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1
		self.add_widget(Label(text="Make Key",halign="center",valign="middle",height=Window.size[0]*0.1,size_hint_y=None,font_size=30))

		self.input_tittle=GridLayout(height=Window.size[0]*0.06,size_hint_y=None)
		self.input_tittle.cols=4
		self.input_tittle.rols=1
		self.input_tittle.add_widget(Label(text="",font_size=20))
		self.input_tittle.add_widget(Label(text="Q",font_size=20))
		self.input_tittle.add_widget(Label(text="m",font_size=20))
		self.input_tittle.add_widget(Label(text="p",font_size=20))



		self.add_widget(self.input_tittle)

		self.input_Qp=GridLayout(height=Window.size[0]*0.1,size_hint_y=None)
		self.input_Qp.cols=4
		self.input_Qp.rols=1
		self.input_Qp.add_widget(Label(text="Please input\nQ m and p"))
		self.input_Q=TextInput()
		self.input_m=TextInput()
		self.input_p=TextInput()
		self.input_Qp.add_widget(self.input_Q)
		self.input_Qp.add_widget(self.input_m)
		self.input_Qp.add_widget(self.input_p)


		self.add_widget(self.input_Qp)

		self.submit_button=Button(text="Submit",height=Window.size[0]*0.06,size_hint_y=None,font_size=20)
		self.submit_button.bind(on_press=self.submit)

		self.add_widget(self.submit_button)

		self.output=Label(text="The Key will be here ~",font_size=20)
		self.add_widget(self.output)

		self.add_widget(back_button())

	def submit(self,instance):
		if not self.input_Q.text.isdigit() or not self.input_m.text.isdigit() or not self.input_p.text.isdigit() :
			self.output.text="Stupid Guy ! ! !   Check Your Input ! ! !"
			return
		print(int(self.input_Q.text),int(self.input_m.text))
		algo.Make_Key(int(self.input_Q.text),int(self.input_m.text),int(self.input_p.text))
		self.output.text="The Key is:\n"+str(algo.Key)
		self.output.halign="center"
		self.output.valign="middle"

class Fast_Key_Exchange(App):
	def build(self):
		self.screen_manager=ScreenManager()

		self.menu_page=menu_page()
		screen=Screen(name="Menu")
		screen.add_widget(self.menu_page)
		self.screen_manager.add_widget(screen)

		self.make_private_code_page=make_private_code_page()
		screen=Screen(name="Make_Priate_Code")
		screen.add_widget(self.make_private_code_page)
		self.screen_manager.add_widget(screen)

		self.make_communication_code_page=make_communication_code_page()
		screen=Screen(name="Make_Communication_Code")
		screen.add_widget(self.make_communication_code_page)
		self.screen_manager.add_widget(screen)

		self.make_key_page=make_key_page()
		screen=Screen(name="Make_Key")
		screen.add_widget(self.make_key_page)
		self.screen_manager.add_widget(screen)

		return self.screen_manager


MyApp=Fast_Key_Exchange()
MyApp.run()