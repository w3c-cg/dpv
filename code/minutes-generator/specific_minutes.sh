#!/usr/bin/env bash

# Check if argument is provided
if [ -z "$1" ]; then
  echo "Usage: '$0 <YY-MM-DD> <irc|txt>' to generate minutes from 'meeting-20<year>-<month>-<date>.<irc|txt>'"
  exit 1
fi

time="$1"
file="meeting-20${time}.$2"
filename="meeting-20${time}"

# check if file exists
if [ ! -f ./data/${file} ]; then
    echo "file ${file} not found"
    exit -1
fi

# Replace with the desired command
perl scribe.perl -implicitContinuations -final -emphasis ./data/${file} > ../../meetings/${filename}.html
echo "Generated ../../meetings/${filename}.html"
