#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using requests package
and displays the response body information.
"""
import requests


if __name__ == "__main__":
    """
    Fetches https://alu-intranet.hbtn.io/status and displays response body info.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
