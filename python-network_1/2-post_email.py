#! /usr/bin/python3
"""
    Request module demonstration comments goes here
"""

import requests
import sys

payload = {
    'email': sys.argv[2]
}

if __name__ == "__main__":
    req = requests.post(sys.argv[1], data=payload)
    print(req.text)
