from kivymd.app import MDApp
from kivy.lang import Builder

KV = """ 
Screen:
    MDToolbar:
        title:'Contacts jbsidis'
        pos_hint:{'top':1}
        md_bg_color: [.2,0,1,.9]
        left_action_items : [["menu", lambda x:print(23)]]
        right_action_items : [["dots-vertical",lambda x:print(234)]]
        elevation:0

    FloatLayout:
        BoxLayout:
            pos_hint: {"center_x": .5, "center_y": .30}
            ScrollView:
                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(60)
                    size_hint_y: .64

                    BoxLayout:
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'account'
                            markup: True
                        TextInput:
                            id: email_jbsidis1
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'phone'
                            markup: True
                        TextInput:
                            id: email_jbsidis2
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Phone"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                        TextInput:
                            id: email_jbsidis3
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Area"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
##                            MDIconButton:
##                                #size_hint: .4, .05
##                                pos_hint: {"center_x": .6, "top": .975}
##                                theme_text_color: "Custom"
##                                text_color: [0,0,0,.8]
##                                icon: 'phone'
##                                markup: True

                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'map-marker'
                            markup: True
                        TextInput:
                            id: email_jbsidis4
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Address"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'a11.png'
                            markup: True
                        TextInput:
                            id: email_jbsidis5
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "State"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                        TextInput:
                            id: email_jbsidis6
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Zipcode"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
##                            MDIconButton:
##                                #size_hint: .4, .05
##                                pos_hint: {"center_x": .6, "top": .975}
##                                theme_text_color: "Custom"
##                                text_color: [0,0,0,.8]
##                                icon: 'phone'
##                                markup: True
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'message'
                            markup: True
                        TextInput:
                            id: email_jbsidis7
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Email"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        MDIconButton:
                            #size_hint: .4, .05
                            pos_hint: {"center_x": .3, "top": .975}
                            theme_text_color: "Custom"
                            text_color: [0,0,0,.8]
                            icon: 'calendar'
                            markup: True
                        TextInput:
                            id: email_jbsidis8
                            height: dp(40)
                            pos_hint: {"center_x": .4, "top": .975}
                            hint_text_color: [0,0,0, 1]
                            foreground_color: [0,0,0,.4]
                            hint_text: "Birthday"
                            background_color: [1,1,1,0]
                            background_image: ""
                            background_normal: ""
                            background_active: ""
                            multiline: False
                            size_hint: .5 ,None #.06
                            canvas.after:
                                Color:
                                    rgba: [0.0039,0.1921,0.2078,1]
                                Line:
                                    width: dp(0.5)
                                    rounded_rectangle:
                                        (self.x, self.y, self.width-dp(20), dp(43),\
                                        dp(8),dp(8),dp(8),dp(8),\
                                        dp(50))
                    
                    BoxLayout:
                        spacing: dp(30)
                        FloatLayout:
                            MDRectangleFlatButton:
                                pos_hint: {'center_x':.3, 'center_y':.5} 
                                text:'Choose'
                                font_size:14
                                halign: "center"
                                on_release: print(root.ids.email_jbsidis1.text,root.ids.email_jbsidis2.text,root.ids.email_jbsidis3.text,root.ids.email_jbsidis4.text,root.ids.email_jbsidis5.text,root.ids.email_jbsidis6.text,root.ids.email_jbsidis7.text,root.ids.email_jbsidis8.text)
                            MDRectangleFlatButton:
                                pos_hint: {'center_x':.7, 'center_y':.5} 
                                text:'Cancel'
                                font_size:14
                                halign: "center"
                                on_release:
                                    root.ids.email_jbsidis1.text=""
                                    root.ids.email_jbsidis2.text=""
                                    root.ids.email_jbsidis3.text=""
                                    root.ids.email_jbsidis4.text=""
                                    root.ids.email_jbsidis5.text=""
                                    root.ids.email_jbsidis6.text=""
                                    root.ids.email_jbsidis7.text=""
                                    root.ids.email_jbsidis8.text=""
                            

                                        
            
    FloatLayout:
        MDIconButton:
            pos_hint: {"center_x": .8, "center_y": 0.945}
            icon: "magnify"
            theme_text_color: "Custom"
            text_color: [1,1,1,1]

"""

class WeatherApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
##    def on_start(self):
##
##        self.root.ids.Test_ss.text = " Dhur bal\nOi salar putera\nMod khaba naki "
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen
WeatherApp().run()
