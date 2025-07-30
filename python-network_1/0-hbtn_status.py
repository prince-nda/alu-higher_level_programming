#!/usr/bin/python3
"""A script that:
- Fetches status from either ALX intranet or a local server.
- Uses urllib for HTTP requests.
"""
import urllib.request
import urllib.error


def fetch_status(url):
    """Fetches and prints the status from a given URL."""
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
            return True
    except urllib.error.URLError:
        return False


if __name__ == '__main__':
    urls = [
        'https://intranet.hbtn.io/status',  # ALX intranet (may require VPN)
        'http://0.0.0.0:5050/status'       # Local fallback
    ]

    for url in urls:
        if fetch_status(url):
            break
    else:
        print("Error: Could not fetch status from any URL.")
