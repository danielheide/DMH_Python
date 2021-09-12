from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineAvatarListItem #ThreeLineIconListItem
from kivymd.uix.list import IconRightWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):

    def build(self):
        screen=Screen()

        scroll=ScrollView()
        list = MDList()

        for i in range(20):
            #icon=IconRightWidget(icon='android')
            image=ImageLeftWidget(source="download.jpg")
            item = ThreeLineAvatarListItem(text='Item '+ str(i+1), secondary_text="this is the item #" + str(i+1),
                                   tertiary_text='this is the detail of the item [the third text ' + str(i+1) + ']')
            #item.add_widget(icon)
            item.add_widget(image)

            list.add_widget(item)

        scroll.add_widget(list)
        screen.add_widget(scroll)
        return screen

DemoApp().run()
