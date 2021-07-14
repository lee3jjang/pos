from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
Window.top = 200
# Window.left = -2300
Window.left = 50

Builder.load_file('signin.kv')

class SigninWindow(BoxLayout):
    pass

class SignApp(App):

    def build(self):
        return SigninWindow()

if __name__ == '__main__':
    sa = SignApp()
    sa.run()
