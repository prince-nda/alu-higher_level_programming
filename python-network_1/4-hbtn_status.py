#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status using requests module."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
    print("\t- utf8 content: {}". format(r.text))
