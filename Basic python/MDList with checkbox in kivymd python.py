from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem,TwoLineAvatarListItem,TwoLineAvatarIconListItem
from kivymd.uix.list import MDList,IconLeftWidget,IconRightWidget,ImageLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox

KV = """
BoxLayout:
    ScrollView:
        MDList:
            id: scroll

    MDRaisedButton:
        id: cm
        text: "Save"
        on_release: app.save_checked2()
"""

selected_item = []
class MainAppjbsidis(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.add_checkboc()

    def check_press_f(self,val, instance_table):
        self.ck_list.append(val)
         

    def save_checked2(self):
        print(self.ck_list)
        self.add_checkboc()
        
    def add_checkboc(self):
        self.ck_list = []
        self.root.ids.scroll.clear_widgets()
        for rec in range(10): 
            items = TwoLineAvatarIconListItem(text=f"iTem {rec}", secondary_text=f"iTem {rec}{rec}")

            right_I = IconRightWidget(icon='nothing.png')
            from functools import partial
            ck = MDCheckbox(active= False)
            ck.bind(on_release=partial(self.check_press_f,rec))
            right_I.add_widget(ck)

            items.add_widget(IconLeftWidget(icon='account'))
            items.add_widget(right_I)

            self.root.ids.scroll.add_widget(items)
                
MainAppjbsidis().run()
