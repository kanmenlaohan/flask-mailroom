import requests
from bs4 import BeautifulSoup


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latin_translation():

    fact = get_fact()
    payload = {"input_text": fact}
    latin_response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data=payload)

    return latin_response.url
