#!/usr/bin/python
import re
import sys
filename=sys.argv[1]
with open(filename, "r") as f:
    text=f.read()
each_word=text.split(' ')
for i in each_word: 
    re_eng=re.search( r'(\+\d{2})\-(\d{2})\-(\d{4})\-(\d{4})', i)
    re_ari=re.search( r'(\d{3})\-(\d{3})\-(\d{4})', i)
    if re_eng:
        eng="%s (%s) %s%s" % (re_eng.group(1), re_eng.group(2), re_eng.group(3), re_eng.group(4))
        print(eng)
    elif re_ari:
        ari="(%s)%s%s" % (re_ari.group(1), re_ari.group(2), re_ari.group(3))
        print(ari)
