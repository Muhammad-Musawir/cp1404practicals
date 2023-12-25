"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder



__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    km_text = StringProperty("0.0")

    def handle_calculate(self):
        try:
            value = float(self.root.ids.input_miles.text)
            result = value * MILES_TO_KM
            self.km_text = f"{result:.2f}"
        except ValueError:
            self.km_text = "0.0"

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        try:
            value = float(self.root.ids.input_miles.text) + change
            self.root.ids.input_miles.text = str(value)
            self.handle_calculate()
        except ValueError:
            self.root.ids.input_miles.text = "0"
            self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
