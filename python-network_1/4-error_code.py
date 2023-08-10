#! /usr/bin/python3
"""
    Request module demonstration comments goes here
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
        exit(1)

    print(req.text)
