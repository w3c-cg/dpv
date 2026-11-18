#!/usr/bin/env python3
#author: Harshvardhan Pandit

import datetime
import glob
# assuming this is run from meetings/generator folder
files = sorted(glob.glob('../../meetings/meeting*.html'), reverse=True)

with open('../../meetings/index.html', 'w') as fd:
    fd.write("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>DPVCG Meeting Minutes</title>
    <style>
        body { max-width: 800px; margin: auto; line-height: 2; font-size: 1.5; }
        ol { list-style: decimal-leading-zero; list-style-position: outside; }
        ol li::before { content: "📅"; display: inline-block; margin-right: 0.2rem; }
    </style>
  </head>
  <body>
    <h1>DPVCG Meeting Minutes</h1>
    <p>purl: <a href="https://w3id.org/dpv/meetings">https://w3id.org/dpv/meetings</a></p>
    <p>See <a href="https://www.w3.org/groups/cg/dpvcg/calendar">W3C DPVCG Calendar</a> for upcoming meetings, agenda, and joining instructions.</p>
    <ol reversed>""")
    for f in files:
        f = f.lstrip('../')
        fdate = f[17:27]
        date = datetime.datetime.strptime(fdate, '%Y-%m-%d')
        date = date.strftime('%d %B %Y %A')
        suffix = f.replace('.html', '').replace(f'meetings/meeting-{fdate}', '')
        if suffix:
          suffix = ' - ' + suffix.replace('-', ' ').lstrip().title()
        fd.write(f'\n<li><a href="{f}">DPVCG Meeting {date}{suffix}</a></li>')
    fd.write("\n</ol></body></html>")

#END
