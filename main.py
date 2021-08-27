from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

def setWall(btn):
    print(btn.btnCount)


class MazeButton(Button):
    background_color = (.1,.1,.1,1)
    def __init__(self, btnCount, **kwargs):
        super(MazeButton, self).__init__(**kwargs)
        self.btnCount = btnCount
        self.wall = False
        self.beginBtn = False
        self.endBtn = False

class MazeScreen(GridLayout):
    cols = 30
    def __init__(self, **kwargs):
        super(MazeScreen, self).__init__(**kwargs)
        btnCount = 0
        for row in range(30):
            for col in range(30):
                btn = MazeButton(btnCount)
                btn.bind(on_press=btnClicked)
                self.add_widget(btn)
                btnCount +=1



class MazeApp(App):
    def build(self):
        return MazeScreen()

if __name__ == '__main__':
    MazeApp().run()
