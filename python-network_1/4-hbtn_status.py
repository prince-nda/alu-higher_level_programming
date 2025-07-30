#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests package.
Displays response body information including type and content.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
    print("\t- utf8 content: {}".format(response.text))  # Added missing line
