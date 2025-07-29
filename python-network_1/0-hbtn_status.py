#!/usr/bin/python3
"""
Module that fetches https://alu-intranet.hbtn.io/status

This module uses urllib to make HTTP requests and displays information
about the response body including its type, raw content, and UTF-8 decoded content.
"""
import urllib.request


def fetch_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status
    and displays information about the response body.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
