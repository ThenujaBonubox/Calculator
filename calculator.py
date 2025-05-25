from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4

        self.display = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.add_widget(self.display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            '='
        ]

        for label in buttons:
            button = Button(text=label, font_size=24)
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)

    def on_button_press(self, instance):
        text = instance.text
        if text == 'C':
            self.display.text = ''
        elif text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = 'Error'
        else:
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
