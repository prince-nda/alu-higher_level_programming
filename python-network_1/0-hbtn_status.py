#!/usr/bin/python3
"""
Module that fetches status from a URL and displays response information.

This module uses urllib to make HTTP requests and displays information
about the response body including its type, raw content, and UTF-8 content.
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
