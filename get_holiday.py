import requests
from bs4 import BeautifulSoup
import datetime


class Holidays:
    def __init__(self):
        self.url = 'https://kakoyprazdnik.com/'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

        self.holidays = self.soup.find_all('h4')
        self.iterator = 0

    def update_holidays(self):
        self.__init__()

    def get_all_holidays(self):
        result = ''
        for holiday in self.holidays:
            result += holiday
        return result

    def return_holidays(self):
        return self.holidays

    def get_holiday(self):
        holiday = self.holidays[self.iterator].text
        self.iterator += 1
        if self.iterator == len(self.holidays) - 1:
            self.iterator = 0
            return "Упс, похоже на сегодня все праздники закончились"
        else:
            return holiday


if __name__ == '__main__':
    print(datetime.date.today())
