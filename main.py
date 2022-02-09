from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


Config.set("graphics", "resizsble", 0)
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 400)



class Application(App):
	
	
	def click(self, instance):
		self.label.text = "on tap"
	
	
	def build(self):
		
		
		
		but_together = BoxLayout()
		grid = GridLayout(cols=1)
		
		
		my_but = Button(text="tap",font_size = 70, background_color="cyan", on_press=self.click)
		my_but2 = Button(text="no tap",font_size = 70, background_color="cyan")
		self.label = Label(text="text",                 font_size = 70)
		
		but_together.add_widget(my_but)
		but_together.add_widget(my_but2)
	
	
		grid.add_widget(but_together)
		grid.add_widget(self.label)
		
		
		
		return grid
		
		
		
		
if __name__ == '__main__':
	Application().run()