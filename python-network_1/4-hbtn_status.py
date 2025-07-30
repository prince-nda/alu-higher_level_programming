#!/usr/bin/python3
"""
This module fetches a status URL using requests package
and displays the response body information.
"""
import requests


if __name__ == "__main__":
    """
    Fetches the status URL and displays response body info.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
