#!/usr/bin/python3
"""Fetches status from either intranet.hbtn.io or local server"""
import urllib.request
import sys

def fetch_status(url):
    """Fetches and displays status from given URL"""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        print("Error fetching status:", e)

if __name__ == "__main__":
    # Default to intranet.hbtn.io if no argument provided
    url = 'http://0.0.0.0:5050/status' if len(sys.argv) > 1 and sys.argv[1] == '--local' \
          else 'https://intranet.hbtn.io/status'
    fetch_status(url)
