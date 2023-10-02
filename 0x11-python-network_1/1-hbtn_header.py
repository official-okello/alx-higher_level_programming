#!/usr/bin/python3
"""Sends a request and displays the value from a URL"""


if __name__ == '__main__':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_res = response.info()
        print(url_res['X-Request-Id'])
