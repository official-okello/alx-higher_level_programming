#!/bin/bash
# sends JSON POST request to a URL and displays the body of the response

curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
