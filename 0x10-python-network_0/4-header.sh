#!/bin/bash
# takes a URL and displays the body of the response

curl -s "$1" -X GET -H "X-School-User-Id: 98"
