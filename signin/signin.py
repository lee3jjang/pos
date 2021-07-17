from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
Window.top = 200
# Window.left = -2300
Window.left = 50

Builder.load_file('signin.kv')

class SigninWindow(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = "[color=#ff0000]username and/or password required[/color]"
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = "[color=#00ff00]Logged In successfully!!![/color]"
            else:
                info.text = "[color=#ff0000]Invalid Username and/or Password[/color]"


class SignApp(App):

    def build(self):
        return SigninWindow()


if __name__ == '__main__':
    sa = SignApp()
    sa.run()
