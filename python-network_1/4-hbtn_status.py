#!/usr/bin/python3
"""A script that:
- Fetches status from https://intranet.hbtn.io/status or http://0.0.0.0:5050/status
- Uses only the requests package
- Displays response body in required format
- PEP 8 compliant
"""
import requests


if __name__ == "__main__":
    # List of URLs to try (in order)
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            # Ensure we got a successful response
            response.raise_for_status()
            
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
            print("\t- utf8 content: {}".format(response.text))
            break
        except requests.exceptions.RequestException:
            continue
    else:
        print("Error: Could not fetch status from any URL.")
