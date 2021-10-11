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


    ScrollView:
        size_hint_y:0.75
        pos_hint: {"center_x": .5, "center_y": .47}
        MDBoxLayout:
            orientation:'vertical'
            size_hint_y:1.7
            spacing:dp(40)
            FloatLayout:
                size_hint: 1,2.2
                pos_hint: {'top':0.99}
                MDLabel:
                    font_style: "H5"
                    theme_text_color: "Primary"
                    text: "Demo Form"
                    halign: 'center'
                    pos_hint: {'center_x':0.5, 'center_y':0.96}

                MDIconButton:
                    icon: "account"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.87}
                MDTextField:
                    hint_text: "Name"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.875}
                    size_hint_x:0.73
                    size_hint_y:0.08
                MDIconButton:
                    icon: "email"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.77}
                MDTextField:
                    hint_text: "Email"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.775}
                    size_hint_x:0.73
                    size_hint_y:0.08
                MDIconButton:
                    icon: "account"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.67}
                MDTextField:
                    hint_text: "Name"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.675}
                    size_hint_x:0.73
                    size_hint_y:0.08
                    on_focus:app.do_it()
                MDIconButton:
                    icon: "email"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.57}
                MDTextField:
                    hint_text: "Email"
                    mode: "rectangle"
                    readonly: True
                    pos_hint: {'center_x':0.425, 'center_y':0.575}
                    size_hint_x:0.465
                    size_hint_y:0.08
                MDRectangleFlatButton:
                    text:'Choose'
                    font_size:13
                    size_hint_y:0.067
                    size_hint_x:0.01
                    # halign: "center"
                    pos_hint:{'center_x':0.83, 'center_y':0.567}

                MDIconButton:
                    icon: "account"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.47}

                MDTextField:
                    hint_text: "Name"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.475}
                    size_hint_x:0.73
                    size_hint_y:0.08
                MDIconButton:
                    icon: "email"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.37}

                MDTextField:
                    hint_text: "Email"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.375}
                    size_hint_x:0.73
                    size_hint_y:0.08

                MDIconButton:
                    icon: "account"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.27}

                MDTextField:
                    hint_text: "Name"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.275}
                    size_hint_x:0.73
                    size_hint_y:0.08

                MDIconButton:
                    icon: "email"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.17}

                MDTextField:
                    hint_text: "Email"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.175}
                    size_hint_x:0.73
                    size_hint_y:0.08

                MDIconButton:
                    icon: "account"
                    halign: 'center'
                    pos_hint: {'center_x':0.08, 'center_y':0.07}

                MDTextField:
                    hint_text: "Name"
                    mode: "rectangle"
                    pos_hint: {'center_x':0.56, 'center_y':0.075}
                    size_hint_x:0.73
                    size_hint_y:0.08
            FloatLayout:
                size_hint: 1,0.2
                pos_hint: {'top':0.7}
                MDRaisedButton:
                    text:'   Submit   '
                    halign: "center"
                    font_size:19
                    size_hint_x:0.92
                    pos_hint:{'center_x':0.504, 'center_y':1}

"""

class WeatherApp(MDApp):

    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen
    def do_it(self):
        print("DHur bal")
WeatherApp().run()
