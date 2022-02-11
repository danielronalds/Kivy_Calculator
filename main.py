#!/usr/bin/env python3
#   ____   _____  _____  _____  _____  __     _____  _____  _____  _____  __     ____   _____
#  |    \ |  _  ||   | ||     ||   __||  |   | __  ||     ||   | ||  _  ||  |   |    \ |   __|
#  |  |  ||     || | | ||-   -||   __||  |__ |    -||  |  || | | ||     ||  |__ |  |  ||__   |
#  |____/ |__|__||_|___||_____||_____||_____||__|__||_____||_|___||__|__||_____||____/ |_____|
#
#  github: https://github.com/danielronalds
#
#  Learning Resource: https://realpython.com/mobile-app-kivy-python/#laying-out-the-ui
#
#  Kivy Calculator App
#

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = False
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current:
                for o in self.operators:
                    if current[-1] == o and button_text == o:
                        return
            new_text = current + button_text
            self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()
