#!/usr/bin/python3
"""A script that:
- Fetches https://intranet.hbtn.io/status.
- Uses the urllib package.
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
