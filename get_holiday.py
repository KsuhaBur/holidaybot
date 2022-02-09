import requests
from bs4 import BeautifulSoup

url = 'https://kakoyprazdnik.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# holidays = soup.find_all('h4')


def get_holidays():
    return soup.find_all('h4')


def get_all_holidays():
    holidays = get_holidays()
    result = ''
    for holiday in holidays:
        result += holiday.text + '\n'
    return result




# if __name__ == '__main__':
#     for holiday in holidays:
#         print(holiday.text)
