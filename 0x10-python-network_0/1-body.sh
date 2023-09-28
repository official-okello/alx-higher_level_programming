#!/bin/bash
# takes in a URL, displays only body of a 200 status code response

curl -s "$1" -X GET -L
