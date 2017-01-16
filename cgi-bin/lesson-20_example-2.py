#!/usr/bin/python3.5

import os
import cgi

def printHeader() :
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Information about system</title></head>")
    print("<body>")
    
def printFooter() :
    print("</body></html>")
    
printHeader()

print("<h2>Query Strings</h2>")

query = os.environ["QUERY_STRING"]

if len(query) == 0 :
    print("<p>Please add some query string.</p>")
else :
    print("<p style='font-style:italic'>The query string is " + cgi.escape(query) + "</p>")
    pairs = cgi.parse_qs(query)
    
    for key, value in pairs.items() :
        print("<p>You set query string '%s' to value %s</p>" % (key, value))

printFooter()
