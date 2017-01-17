#!/usr/bin/python3.5

import cgi

def printHeader() :
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Forms with CGI Python - POST</title></head>")
    print("<body>")
    
def printFooter() :
    print("</body></html>")
    
printHeader()

print("<h2>Form with POST Method</h2>")

print("<form method='POST' action='lesson-21_example-2.py'>")
print("<p><input type='radio' name='rblSex' value='Male'>Male<br>")
print("<input type='radio' name='rblSex' value='Female'>Female<br>")
print("<br>")
print("<input type='submit' value='Submit' /></p></form>")

pairs = cgi.parse()

if "rblSex" in pairs :
    print("<p>Yout sex is: %s</p>" % cgi.escape(pairs["rblSex"][0]))

printFooter()