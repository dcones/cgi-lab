#!/usr/bin/env python3
import cgi, cgitb, os
cgitb.enable()


print("Content-Type: text/plain\n\n")
print(os.environ)
