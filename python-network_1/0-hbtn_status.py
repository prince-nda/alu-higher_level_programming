#!/usr/bin/python3
"""A script that:
- Fetches https://intranet.hbtn.io/status
- Uses urllib package
- Displays the response body in a specific format
"""
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error fetching status:", e)
