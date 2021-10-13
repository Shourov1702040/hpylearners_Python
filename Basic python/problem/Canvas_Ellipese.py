from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size=(347,615)

KV = """ 
MDScreen:
    MDToolbar:
        title:'My Demo App'
        pos_hint:{'top':1}
        left_action_items : [["arrow-left"]]
        right_action_items : [["dots-vertical"]]
        elevation:15
                
    FloatLayout:
        canvas:
            Color:
                rgba: (1, 1, 1, 1)
            Ellipse:
                id: imga
                pos: 60, 280
                size: 200 , 210 
                # source: ''
                angle_start: 0
                angle_end: 360

"""

class WeatherApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def on_start(self):
        self.root.ids.imga.source= 'D:/Working_dir/Programming/Python/Kivy-MD/User_images/amber.jpg'

WeatherApp().run()
