#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests package."""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
    print("\t- utf8 content: {}".format(response.text))
