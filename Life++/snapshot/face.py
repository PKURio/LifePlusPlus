# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import sys
import json
face_token_lis = ["f574f4292f0a6ee0c9ea787af637fc40", 
"a229310365480c3904471e9e38480d47", 
"2c60bc7669936a76551d2b0dcf9a2ffe",
"17b1edd7b5e5d0bf1951d25294e7e68c",
"65afcebe4d83d18541214b5db655bbf7"]
http_url_search='https://api-cn.faceplusplus.com/facepp/v3/search'
key = "6vnqJG0OT_62fjICgNINbvX6h9midmzy"
secret = "OQ-E3XWvUHNLbAX5CtLXVrI9vj3shAIO"
filepath = sys.argv[1]
faceset_token = "7a042ad9f24c80a02227d4fcb5d5fb0f"
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
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'faceset_token')
data.append(faceset_token)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append("gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url_search)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
res = -1
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	tmp_qrcont = json.loads(qrcont)
	if tmp_qrcont.has_key("results"):
		tmp_confidence = json.loads(qrcont)["results"][0]["confidence"]
		tmp_face_token = json.loads(qrcont)["results"][0]["face_token"]
		if tmp_confidence < 60:
			print -1
		else:
			res = face_token_lis.index(tmp_face_token)
			print res + 10
	else:
		print -1
except urllib2.HTTPError as e:
    print e.read()