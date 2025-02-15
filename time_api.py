import requests
from bs4 import BeautifulSoup


def time():
    response = requests.get("https://www.unixtimestamp.com/")
    time_soup = BeautifulSoup(response.content, "html.parser")
    epoch_time = time_soup.find_all("h3", class_="text-danger")

    return epoch_time[0].getText().split()[0]
