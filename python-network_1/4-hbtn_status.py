#!/usr/bin/python3
"""Fetches status from either:
- https://intranet.hbtn.io/status (primary)
- http://0.0.0.0:5050/status (fallback)
using requests package.
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
