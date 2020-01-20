#!/usr/bin/python3
import requests

website = "http://158.69.76.135/level0.php"
preference = {'id':'1149', 'holdthedoor': 'Submit'}

if __name__ == "__main__":
    for i in range(1, 1025):
        requests.post(website, data=preference)
    print("Done !!")
