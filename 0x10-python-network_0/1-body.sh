#!/bin/bash
# takes in a URL, sends GET requestt to the URL, and displays the body of the response
curl -s "$1" -X GET -L
