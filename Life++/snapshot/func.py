# -*- coding: utf-8 -*-
# We have applied those functions:
#-----1. send a 'SOS' message and sound the alarm
#-----2. play a certain music
#-----3. say words that are stored in txt
#-----4. auto reply in WeChat

from aip import AipSpeech
from wxpy import *
from twilio.rest import Client
import mp3play
import pygame
import time
import sys
import pyttsx
import json
import requests

reload(sys)
sys.setdefaultencoding('utf8')

emotion = sys.argv[1]

def error(error_message = 'error'):
	print error_message
	exit(1)

def send_message(message, to_number):
    account_sid = "AC0be3133faec61b5c4b9c9232d60d3ce4"
    auth_token = "ae4dad02fdf19cf97804a974c6371a82"   
    twilioNumber = '+14843948124'
    client = Client(account_sid, auth_token)
    message = client.messages.create(to = to_number, from_ = twilioNumber, body = message)

def music_player(music_path = './somethingJustLikeThis.mp3'):
	clip = mp3play.load(music_path)
	clip.play()
	print clip.seconds()
	time.sleep(clip.seconds())
	clip.stop()

def say_words(path = './idea.txt'):
	with open(path,'r') as file:
		text = file.read()
	APP_ID = "11230570"
	API_KEY = "FjqL9yeCq7McbQva0BcFZhaS"
	SECRET_KEY = "d2bd8fdfcbebb95a141343ebd81d2f75"
	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	result = client.synthesis(text, 'zh', 1, {
    	'vol': 5,
	})
	music_path = './audio.mp3'
	if not isinstance(result, dict):
		with open(music_path, 'wb') as f:
			f.write(result)
		music_player(music_path)

def auto_reply(text):     
    url = "http://www.tuling123.com/openapi/api"
    api_key = "e20830d1d44b4521bf82b44f3f325d95"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data = json.dumps(payload))     
    result = json.loads(r.content)     
    return "[this is a bot:] " + result["text"] + "~~~"

def reply_wechat():
	bot = Bot(cache_path = True)
	bot.file_helper.send("hello")
	my_friend = bot.friends()
	@bot.register(my_friend, TEXT)
	def print_others(msg):
		print(msg)
		return auto_reply(msg.text)
	embed()

def function(emotion = 5):
	if emotion not in range(1, 8):
		error('error: Wrong Emotion')
	elif emotion == 1 or emotion == 3:	#anger, fear
		send_message(r'SOS！救命！我被困在北大了！', '+8613161321277')
		music_player('http://data.huiyi8.com/2017/gha/03/20/2032.mp3')
	elif emotion == 2 or emotion == 7:	#disgust, surprise
		reply_wechat()
	elif emotion == 4:	#happiness
		music_player()
	elif emotion == 6:	#sadness
		say_words()
	elif emotion == 5:	#neutral
		pass
		
if __name__ == '__main__':
    function(int(emotion) - 10)