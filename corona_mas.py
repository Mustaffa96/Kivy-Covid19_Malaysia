from lxml.html import fromstring
from requests import get
from re import sub


class coronaMas:
    def __init__(self):  # initial method
        self.load_info()  # calling a method to refresh the information

    def load_info(self):  # defining a function that will refresh the information
        self.corona_dict = {}  # defining an empty dictionary which will contain the data

        self.page = get(
            "https://www.worldometers.info/coronavirus/country/malaysia/")  # getting data from the html page
        self.page = fromstring(self.page.content)  # parsing the html page

        self.total_cases = self.page.xpath("//div[4]/div/span/text()")
        self.total_cases = self.total_cases[0]
        self.corona_dict['total cases'] = self.total_cases

        self.death_cases = self.page.xpath("//div[5]/div/span/text()")
        self.death_cases = self.death_cases[0]
        self.corona_dict['deaths'] = self.death_cases

        self.cured_cases = self.page.xpath("//div[6]/div/span/text()")
        self.cured_cases = self.cured_cases[0]
        self.corona_dict['recovered'] = self.cured_cases

        self.update_date = self.page.xpath("//div[@style ='font-size:13px; color:#999; text-align:center']/text()")
        self.update_date = self.update_date[0]
        self.update_date = self.update_date.strip()  # removing the unwanted spaces from the date
        self.corona_dict['update date'] = self.update_date

    def print_info(self):  # defining a method that will print the data stored
        self.printed_text = f"""    
        Update : {self.corona_dict['update date']}
    
        Total cases : {self.corona_dict['total cases']}
    
        Deaths : {self.corona_dict['deaths']}
    
        Recovered : {self.corona_dict['recovered']}
    
        """  # defining a variable that will add the data to a text

        print(self.printed_text)  # printing the text with the data added


if __name__ == "__main__":
    coronaMas().print_info()  # only print the text if the class is executed directly and not imported
