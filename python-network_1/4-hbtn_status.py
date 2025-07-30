#!/usr/bin/python3
"""Status checker script using requests module.

Fetches status from either:
- https://intranet.hbtn.io/status (primary)
- http://0.0.0.0:5050/status (fallback)
and displays the response in the required format.
"""
import requests


if __name__ == "__main__":
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises exception for 4XX/5XX status
            
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
            print("\t- utf8 content: {}".format(response.text))
            break
        except requests.exceptions.RequestException:
            continue
    else:
        print("Error: Could not fetch status from any URL.")
