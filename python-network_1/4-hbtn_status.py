#!/usr/bin/python3
"""A script that:
- Fetches status from https://intranet.hbtn.io/status or http://0.0.0.0:5050/status
- Uses urllib package
- Displays response body in required format
"""
import urllib.request
import urllib.error


if __name__ == "__main__":
    urls = [
        'https://alx-intranet.hbtn.io/status',  # Primary URL
        'http://0.0.0.0:5050/status'           # Fallback URL
    ]
    
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                content = response.read()
                print("Body response:")
                print("\t- type: {}".format(type(content)))
                print("\t- content: {}".format(content))
                print("\t- utf8 content: {}".format(content.decode('utf-8')))
                break
        except urllib.error.URLError:
            continue
    else:
        print("Error: Could not fetch status from any URL.")
