
"""
Delta electro code
Md Touhid Islam
Depertment of CSE, HSTU
https://www.facebook.com/Shourov40
"""


import urllib.request as urec

def check_connection():
	host = "http://www.google.com"
	try:
		urec.urlopen(host)
		return True
	except :
		return False

if check_connection():
	print("Connected to a network")
else:
	print("No internet")
  
  
  
  
  
