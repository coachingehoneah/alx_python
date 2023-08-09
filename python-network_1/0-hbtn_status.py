"""
Script that fetches a given url
"""

import requests

res = requests.get("https://intranet.hbtn.io/status")

returned_type = type(res.text)
content = res.text

if __name__ == "__main__":

    print("Body response:")
    print("\t- type: {}".format(returned_type))
    print("\t- content: {}".format(content))
