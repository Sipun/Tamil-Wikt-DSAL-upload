#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re

i = 1
while i != 100000:
    urls = "http://dsalsrv02.uchicago.edu/cgi-bin/romadict.pl?page=" + str(i) +"&table=winslow&display=utf8"
    request = urllib2.Request(urls)
    handle = urllib2.urlopen(request)
    content = handle.read()
    splitted_page = content.split("</a></div><P>", 1);
    splitted_page = splitted_page[1].split("<table width=", 1)
    art = splitted_page[0] #getting html content
    art = art.replace('<span style="font-size:larger">', "\nstart\n----------------------\n\n'''") #begining of a article
    art = art.replace('</blockquote></P>', "\n\n----------------------\nend\n") #end of a article
    art = art.replace('</tam>,</span>', "'''\n\n== meaning ==\n") #putting header
    art = art.replace(' [', "[")
    art = art.replace("'''*", "'''")
    art = re.sub('\<.*?\>','', art) #removing unnecessary html codes
    print art

    i+=1
