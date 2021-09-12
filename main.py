from kivymd.app import MDApp
from kivy.lang import Builder
#from kivy.core.window import Window

#Window.size = (300, 500)

navigation_helper = """
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'me.jpg'

                MDLabel:
                    text: '   Daniel'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: '    heide.daniel@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'folder' 
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()