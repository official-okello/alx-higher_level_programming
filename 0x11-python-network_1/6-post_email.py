#!/usr/bin/python3
""" Sends a POST request to URL, displays the body of the response"""


if __name__ == "__main__":
    import sys
    import requests

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
