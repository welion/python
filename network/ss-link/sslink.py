### This python program used to get https://www.ss-link.com ###

#!/usr/bin/env python


import cookielib
import urllib
import urllib2
import re
import os
import subprocess

EMAIL = 'email'
PASSWD = 'password'
USER_EMAIL = '353566165@qq.com'
USER_PASSWD = '83da6d49515184510b37e8f86269e93f'

SSLINK_LOGIN = 'https://www.ss-link.com/login'
SSLINK = 'https://www.ss-link.com/my/free'

# To get cookie_info 

def extract_cookie_info():
	"""Fake login to a site with cookie"""
	# Setup cookie jar
	cj = cookielib.CookieJar()
	login_data = urllib.urlencode({EMAIL : USER_EMAIL,
					'redirect':'/my',
					PASSWD : USER_PASSWD})
	# Create url opener
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	resp = opener.open(SSLINK_LOGIN , login_data)


	resp = opener.open(SSLINK)
	html_page = resp.read()
	
	IPs = re.findall('<td>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td>',html_page)
	PORTs = re.findall('<td>\d{2,4}</td>',html_page)
	PASSWORDs = re.findall('<td>\d{7,8}</td>',html_page)

	IP = re.sub('<td>|</td>','',IPs[3])
	PORT = re.sub('<td>|</td>','',PORTs[1])
	PASSWORD = re.sub('<td>|</td>','',PASSWORDs[1])

	if IP is not None and PORT is not None and PASSWORD is not None:

		json_info = "{\n" + "\t\"server\" : \""+ IP + "\",\n" + "\t\"server_port\" : "+ PORT + ",\n" + "\t\"local_port\" : 8888, \n" + "\t\"password\" : \"" + PASSWORD + "\",\n" + "\t\"method\" : \"aes-256-cfb\",\n" +"\t\"remarks\" : \"\"\n\t }"	
		return json_info
	return None
	
if __name__=='__main__':

	ping_result = os.system('ping -c 4 8.8.8.8')
	if ping_result == 0:	
		json_file = extract_cookie_info()
		if json_file is not None:
			
			with open("/root/config.json","w") as f:
				f.write(json_file)
			os.system('/usr/local/bin/sslocal -c /root/config.json')

