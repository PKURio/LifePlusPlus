# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import json
import sys
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "***"
secret = "***"
filepath = sys.argv[1]
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)

data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)

data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()

data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')

data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append("beauty")
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	info = json.loads(qrcont)
	# print([k for k in info.keys()])
	# print([k for k in info['faces'][0].keys()])

	female_score = info['faces'][0]['attributes']['beauty']['female_score']
	male_score = info['faces'][0]['attributes']['beauty']['male_score']

	print female_score
	print male_score

except urllib2.HTTPError as e:
    print e.read()
