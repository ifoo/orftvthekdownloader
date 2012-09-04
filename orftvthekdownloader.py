# ugly 06:00-in-the-morning-hack
# clean up!!

# Usage: orftvthekdownloader.py TVTHEKURL
# e.g: python orftvthekdownloader.py http://tvthek.orf.at/programs/4450921-Sommergespraeche-2012/episodes/4558937-Sommergespraeche

# needs mplayer to download MMS stream to file

import urllib2
import subprocess
import sys

data = urllib2.urlopen(sys.argv[1]).read()

for l in data.split("\n"):
	if l.find("URL") > -1 and l.find(".asx") > -1:
		asxurl = l.split("\"")[3]

		data2 = urllib2.urlopen("http://tvthek.orf.at" + asxurl).read()
		ps = data2.find("mms")
		wmvurl = data2[ps:].split("\"")[0]
		print wmvurl
		su = tvthek_url.split("programs/")[1].split("/")[0]
		ps = su.find("-")
		su = su[ps+1:]
		subprocess.call(['/usr/bin/mplayer', '-dumpfile', su+'.wmv', '-dumpstream', wmvurl])
