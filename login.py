#!/usr/bin/env python3
import cgi, cgitb, secret, os
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie
cgitb.enable()


res = cgi.FieldStorage()
username = res.getfirst("username")
password = res.getfirst("password")
print("Content-Type: text/html")

form_ok = username==secret.username and password==secret.password

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_user = None
c_pass = None
if c.get("username"):
	c_user = c.get("username").value
if c.get("password"):
	c_pass = c.get("password").value

cookie_ok = c_user ==secret.username and c_pass==secret.password
if cookie_ok:
	username = c_user
	password = c_pass

if form_ok:
	print("Set-Cookie: username=", username)
	print("Set-Cookie: password=", password)

#print()
#print(login_page())
if not username and not password:
	print(login_page())
elif username==secret.username and password==secret.password:
	print(secret_page(username, password))
else:
	print(after_login_incorrect())
