#!/usr/bin/python3.5

import cgi

def printHeader() :
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head><title>Forms with CGI Python - GET</title></head>")
    print("<body>")
    
def printFooter() :
    print("</body></html>")
    
printHeader()

print("<h2>Form with GET Method</h2>")

print("<form method='GET' action='lesson-21_example-1.py'>")
print("<p>Company:<input type='text' name='txtCompany' />")
print("<br>")
print("<input type='submit' value='Submit' /></p></form>")

pairs = cgi.parse()

if "txtCompany" in pairs :
    print("<p>Yout company is: %s</p>" % cgi.escape(pairs["txtCompany"][0]))

printFooter()