#!/usr/bin/python
#coding=utf-8

import cookielib
import urllib2
import urllib
import json

Hosts = 'http://lock.mobi.qihoo.net:3000'
cookiejar = None
urlOpener = None


def getMethod(URI,params):
	try:
		url = Hosts+URI+"?"
		for key in params:
			if type(params[key])==dict:
				param = json.dumps(params[key])
				paramsStr = "%s=%s" %(key,param)
			else:	
				paramsStr = "%s=%s" %(key,str(params[key]))
			url = url + paramsStr
		req = urllib2.Request(url)
		return req
	except Exception,e:
		print e
	
def postMethod(URI,params):
	try:
		url = Hosts+URI
		postData = urllib.urlencode(params)
		req = urllib2.Request(url,postData)
		return req
	except Exception,e:
		print e
		

if __name__=='__main__':
	cookiejar = cookielib.CookieJar()
	urlOpener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

	URI = "cashjewel/getuserinfo"
	getParams = {
		'prz_ids':{"prz_ids":[11,12,13]}
	}
	NoneParams = {}
	#req = getMethod(URI,NoneParams)

	URI = "/lock/theme/list"
	postParams = {
		'typeid':2,
		'lastid':-1,
		'num':2
	}
	req = postMethod(URI,postParams)
	req.add_header('Cookie','Q=u%3Dfhfrnzvg%26n%3D%26le%3D%26m%3DZGZ1WGWOWGWOWGWOWGWOWGWOZwZj%26qid%3D2636087498%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_bbs%26t%3D1; T=s%3D00e3bf80852d1ef62647a62e2684808f%26t%3D1462525348%26lm%3D%26lf%3D2%26sk%3Dee29feb7c380d81b3cb3096d744f88e1%26mt%3D1462525348%26rc%3D%26v%3D2.0%26a%3D1')
	res = urlOpener.open(req)
	print res.read()
