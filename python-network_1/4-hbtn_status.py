#!/usr/bin/python3
"""
Module that fetches status from a URL using requests package.

This module uses the requests library to make HTTP requests and displays
information about the response body including its type and content.
The response text is automatically decoded by requests into a string.
"""
import requests


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
