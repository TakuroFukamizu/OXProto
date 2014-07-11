#!/usr/bin/python
# coding: UTF-8
import urllib
import urllib2

'''
back_url
	011 : https://www.web-odakyu.com/mb/R011.do?STICKY=11074
	020 : https://www.web-odakyu.com/mb/R020_01.do?back_url=020&STICKY=11074
'''
'''
url = 'https://www.web-odakyu.com/mb/R011.do?STICKY=11074'
values = {
	'back_url' : '011',
	'req_knd'  : '0',
	'LoginKbn' : 'C',
	'account'  : '3439802',
	'password' : '0212'
}
'''
# R100
url = 'https://www.web-odakyu.com/mb/R100.do?STICKY=11074'
values = {
	'back_url' : '011',
	'req_knd'  : '0',
	'LoginKbn' : 'C',
	'account'  : '3439802',
	'password' : '0212'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
html = response.read()

print(len(html))
f = open('R020.html', 'w')
f.write(html)
f.close()