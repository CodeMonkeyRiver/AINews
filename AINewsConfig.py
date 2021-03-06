# This file is part of NewsFinder.
# https://github.com/joshuaeckroth/AINews
#
# Copyright (c) 2011 by the Association for the Advancement of
# Artificial Intelligence. This program and parts of it may be used and
# distributed without charge for non-commercial purposes as long as this
# notice is included.

"""
AINewsConfig reads the configure file: config.ini.
It parses the config.ini as well as pre-define several static parameters.
"""

import sys
from AINewsTools import loadconfig, loadfile

# Load those user configurable parameters
config = loadconfig("config/config.ini")

# Load db parameters
db = loadconfig("config/db.ini")

# Load paths
paths = loadconfig("config/paths.ini")

whitelist = []
for line in loadfile(paths['ainews.whitelist']):
    w = line.strip()
    if w != '':
        whitelist.append(w)

blacklist_urls = []
for line in loadfile(paths['ainews.blacklist_urls']):
    w = line.strip()
    if w != '':
        blacklist_urls.append(w)

blacklist_words = []
for line in loadfile(paths['ainews.blacklist_words']):
    w = line.strip()
    if w != '':
        blacklist_words.append(w)

stopwords = set()
try:
    file = open(paths['ainews.stoplist'], "r")
except IOError:
    print "Fail to open stop-list file"
else:
    for word in file.readlines():
        stopwords.add(word.rstrip())
    file.close()


"""
Regular expression used to extract the date from text
key: dateformat
value: (regular expression, time str parsing)
"""
dateformat_regexps = {
    "Mon. DD, YYYY" : ("(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\. (0?[1-9]|[12][0-9]|3[01]), 20\d\d", "%b. %d, %Y"),
    "Mon DD, YYYY" : ("(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0?[1-9]|[12][0-9]|3[01]), 20\d\d","%b %d, %Y"),
    "Month DD, YYYY" : ("(January|February|March|April|May|June|July|August|September|October|November|December) (0?[1-9]|[12][0-9]|3[01]), 20\d\d", "%B %d, %Y"),  
    "DD Month, YYYY" : ("(0?[1-9]|[12][0-9]|3[01]) (January|February|March|April|May|June|July|August|September|October|November|December), 20\d\d", "%d %B, %Y"),
    "DD Month YYYY" : ("(0?[1-9]|[12][0-9]|3[01]) (January|February|March|April|May|June|July|August|September|October|November|December) 20\d\d", "%d %B %Y"),
    "Mon DD YYYY" : ("(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0?[1-9]|[12][0-9]|3[01]) 20\d\d", "%b %d %Y"),
    "Month DD YYYY" : ("(January|February|March|April|May|June|July|August|September|October|November|December) (0?[1-9]|[12][0-9]|3[01]) 20\d\d","%B %d %Y"),
    "YYYY-MM-DD" : ("20\d\d\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])", "%Y-%m-%d"),
    "MM/DD/YYYY" : ("(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/(19|20)\d\d", "%m/%d/%Y"),
    "DD Mon YYYY" : ("(0?[1-9]|[12][0-9]|3[01]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) 20\d\d", "%d %b %Y"),
    "DD/MM/YYYY" : ("(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/20\d\d","%d/%m/%Y")
}

