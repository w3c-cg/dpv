#!/usr/bin/env python3

import argparse
import tempfile
import urllib.request

from icalendar import Calendar

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

url = args.url.rstrip("/") + "/export"

with tempfile.NamedTemporaryFile() as f:
    urllib.request.urlretrieve(url, f.name)

    with open(f.name, "rb") as fp:
        cal = Calendar.from_ical(fp.read())

    for component in cal.walk():
        if component.name == "VEVENT":
            # print(component.get("DESCRIPTION"))
            description = str(component.get("DESCRIPTION"))
            break

lines = description.splitlines()

# Ignore first line and any empty lines after it
lines = lines[1:]
while lines and not lines[0].strip():
    lines.pop(0)

agenda = ""
output = []

for line in lines:
    line = line.strip()

    if not line:
        continue

    if line.startswith("agenda:"):
        agenda = line
        continue

    if line.startswith("#"):
        output.append(f"Topic: {line[1:].strip()}")
        output.append("")
        continue

    if line.startswith("- "):
        text = line[2:].strip()

        words = text.split()
        url = None
        remaining = []

        for word in words:
            if word.startswith("http://") or word.startswith("https://"):
                url = word
            else:
                remaining.append(word)

        output.append(f"Subtopic: {' '.join(remaining)}")

        if url:
            output.append(url)

        output.append("")
        continue

for line in output:
    print(line)