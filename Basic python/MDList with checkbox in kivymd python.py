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
        for rec in range(10): 
            items = TwoLineAvatarIconListItem(text=f"iTem {rec}", secondary_text=f"iTem {rec}{rec}",on_release=self.save_checked)

            items.add_widget(IconLeftWidget(icon='account'))
            items.add_widget(IconRightWidget(icon='all.png'))
            # ck = MDCheckbox(on_active=self.save_checked)
            # items.add_widget(IconRightWidget(ck))
            self.root.ids.scroll.add_widget(items)

    def save_checked(self,x):
        print('OK')
                
    def save_checked2(self):
        print('OK')
                
MainAppjbsidis().run()
