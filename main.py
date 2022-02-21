from kivy.app import App
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock

from threading import Thread

from corona_mas import coronaMas


#   print(coronaLeb().corona_dict['recovered'])
#   str(coronaLeb().corona_dict[""])


class MyGrid(Widget):

    def __init__(self, **kwargs):  # initial method
        super(MyGrid, self).__init__(**kwargs)  # defining a parent class

        # self.change_text()   #calling the method to change the text

        # Clock.schedule_once(self.change_text, 1)   #after 1 second execute the specified function

        self.text_thread = Thread(target=self.change_text)  # loading the info on a different thread to reduce the time
        self.text_thread.start()  # starting the thread

    def change_text(self):  # defining a method that will update the text in the app
        self.ids.update_date.text = str(coronaMas().corona_dict["update date"])  # for each specific id defined in the kv file the text will be updated depending on the data stored in the dictionary
        self.ids.total_cases_box.text = str(coronaMas().corona_dict["total cases"])
        self.ids.deaths_box.text = str(coronaMas().corona_dict["deaths"])
        self.ids.reco_cases_box.text = str(coronaMas().corona_dict["recovered"])


class MyApp(App):
    title = "Corona Malaysia"  # setting the window title

    #Config.set('graphics', 'width', '400')  # setting the window dimensions
    #Config.set('graphics', 'height', '600')

    def build(self):
        return MyGrid()  # calling the class that will build the app


if __name__ == "__main__":
    MyApp().run()  # running the app to open the window
