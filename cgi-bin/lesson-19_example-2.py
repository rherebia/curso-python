#!/usr/bin/python3.5

import time

print("Content-Type:text/html")
print()
print("<html>")
print("<head><title>Current Date and Time</title></head>")
print("<body>")
print("<br>")
print("<h3><center>" + time.ctime(time.time()) + "</center></h3>")
print("</body>")
print("</html>")