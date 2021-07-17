from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivystudio import KivyStudio

class OperatiorWindow(BoxLayout):
    
    def __init__(self, **kwrags):
        super().__init__(**kwrags)


class OperatorApp(App):

    def build(self):
        return OperatiorWindow()


if __name__ == '__main__':
    studio = KivyStudio('operator/operator.kv')
    studio.run()
    # oa = OperatorApp()
    # oa.run()
