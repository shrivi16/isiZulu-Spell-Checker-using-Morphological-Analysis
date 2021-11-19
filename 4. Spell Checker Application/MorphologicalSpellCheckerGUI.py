# This creates a GUI for our spell checker application

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import SpellCheckingAlgorithm


class IsizuluSpellChecker(App):
    def build(self):

        # Window.clearcolor = (0, 0, 0, 0)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Image
        self.window.add_widget(Image(source="logo2.png"))

        # Space
        self.space = Label(text="",
                            color="#000000",
                            halign="center",
                            size_hint=(0.3, 0.3),
                            font_size=22)
        self.window.add_widget(self.space)

        # Text Input
        self.user = TextInput(multiline = False,
                              font_size = 22,
                              hint_text = "Enter a word",
                              padding_y = (20, 20),
                              size_hint = (0.2, 0.6),
                              halign = "center",
                              background_normal ="",
                              cursor_color = "#000000")
        self.window.add_widget(self.user)

        # Button
        self.button = Button(text="Check Spelling",
                             font_size=22,
                             size_hint = (0.6, 0.6),
                             halign="center",
                             background_color = "#111111",
                             background_normal="")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Answer - Correct or Not?
        self.answer = Label(text="",
                            color="#000000",
                            halign="center",
                            size_hint=(0.7, 0.7),
                            font_size=36)
        self.window.add_widget(self.answer)

        # Segmentation
        self.segment = Label(text="",
                             color=[1, 1, 1, 1],
                             halign="center",
                             size_hint=(0.6, 0.6),
                             font_size=30)
        self.window.add_widget(self.segment)

        return self.window


    def callback(self, instance):
        word = self.user.text
        word = word.lower()
        correct, seg = SpellCheckingAlgorithm.result(word)

        if correct:
            self.answer.color = "#00FF00"
            self.answer.text = "Correct"
            self.segment.text = self.user.text + " = " + seg
        else:
            self.answer.color = "#FF0000"
            self.answer.text = "Incorrect"
            self.segment.text = seg

if __name__ == "__main__":
    IsizuluSpellChecker().run()
