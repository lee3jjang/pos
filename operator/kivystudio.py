from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.utils.hot_reload_viewer import HotReloadViewer

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

Screen:
    BoxLayout:
        CodeInput:
            id: code
            lexer: KivyLexer()
            style_name: "native"
            size_hint_x: .6
        HotReloadViewer:
            size_hint_x: .4
            path: app.path_to_kv_file
            errors: True
            errors_text_color: 1, 1, 0, 1
            errors_background_color: app.theme_cls.bg_dark
'''

class KivyStudio(MDApp):
    
    def __init__(self, path_to_kv_file, **kwargs):
        super(KivyStudio, self).__init__(**kwargs)
        self.path_to_kv_file = path_to_kv_file
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, *args):
        if (args[3]=='s') and ('ctrl' in args[4]):
            self.update_kv_file(self.screen.ids.code.text)
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)
        with open(self.path_to_kv_file, "r") as kv_file:
            self.screen.ids.code.text = kv_file.read()
        return self.screen

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)