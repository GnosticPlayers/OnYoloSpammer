#!/usr/bin/env python3

#Coded By GnosticPlayers

import os
import sys
import time
import json
import requests

def clear():
	responce = os.system("clear")

def welcome_banner():
	print('''
		   _____ _                              _ 
		  / ____| |                            | |
		 | |    | | _____      ___ __   ___  __| |
		 | |    | |/ _ \ \ /\ / / '_ \ / _ \/ _` |
		 | |____| | (_) \ V  V /| | | |  __/ (_| |
		  \_____|_|\___/ \_/\_/ |_| |_|\___|\__,_|
				@GnosticPlayers      
		''')


clear()
welcome_banner()

url = input("[!] Enter the URL to the onyolo: ")
url = url + "/message"
filee = False
Spamm = False

if "-f" in sys.argv:
	try:
		File = sys.argv[sys.argv.index("-f")+1]
		File = open(File,"r")
		filee = True
	except:
		print("Something went wrong")
		sys.exit()

elif "-s" in sys.argv:
	try:
		spam = input("[~]All messages sent to OnYolo that are seen as harassment will not be sent.\n[!] Please enter your message: ")
		numSpam = input("Enter how many messages to spam (0 for endless spam):  ")
		numSpam = int(numSpam)
		Spamm = True
	except:
		print ("something went wrong")
		sys.exit()

elif "-h" in sys.argv:
	print ("""
the two different options you can choose from for this tool is either loading a file with custom messages or
spamming one singular message that wont stop until you chose it to.

args:

-s = spams user with a custom message until you stop it
-f = choose a file with custom messages to spam

examples:

python onyolospammer.py -s
python onyolospammer.py -f filename.txt""")

else:
		print ("""
the two different options you can choose from for this tool is either loading a file with custom messages or
spamming one singular message that wont stop until you chose it to.

args:

-s = spams user with a custom message until you stop it
-f = choose a file with custom messages to spam

examples:

python onyolospammer.py -s
python onyolospammer.py -f filename.txt""")

#im pretty sure you dont even need these but idk. The referrer is always wrong but it still spams people
headers = {'origin':"https://www.onyolo.com",
		   'accept-encoding':"gzip, deflate, br",
		   'accept-language':"en-US,en;q=0.9",
		   'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
		   'content-type':"application/json;charset=UTF-8",
		   'accept':"application/json, text/plain, */*",
		   'referrer':"https://www.onyolo.com/bu7y7i2ajX",
		   'cookie':"popshow-temp-id=t77q4i55wabtmldluy9rp8",
		   'content-length': "75"}

if filee == True:
	for line in File:
		data = {'text': line,
		         'cookie':"1qwgsmde9wvjlteue7nhtdk"} #just some random cookie number
		data_json = json.dumps(data)
		try:
			a = requests.post(url,data=data_json,headers=headers,timeout=3)
		except requests.exceptions.ReadTimeout:
			print ("We got hit with a request timeout. Restarting in 2 seconds")
			continue
		if a.status_code == 200:
			print ("The message: [" + line + "] has been sent to victim!")
			time.sleep(0.1)
		else:
			print ("Something went wrong with message: " + line + " - idk what happened")
			print (a.status_code)
			continue

elif Spamm == True:
	try:
		if numSpam == 0:
			sent = 0
			while numSpam < 3:
				data = {'text': spam,
					'cookie':"1qwgsmde9wvjlteue7nhtdk"} #just some random cookie number
				data_json = json.dumps(data)
				try:
					a = requests.post(url,data=data_json,headers=headers,timeout=3)
				except requests.exceptions.ReadTimeout:
					print ("We got hit with a request timeout. Restarting in 2 seconds")
					continue
				if a.status_code == 200:
					print (str(sent) + ".) The message: [" + spam + "] has been sent to victim!")
					time.sleep(0.1)
					sent += 1
				else:
					print ("Something went wrong with message: " + spam + " - idk what happened")
					print (a.status_code)
					continue
	except KeyboardInterrupt:
		print ("Exiting script")
		sys.exit()

	else:
		sent = 0
		for num in range(1,numSpam):
			data = {'text': spam,
		         'cookie':"1qwgsmde9wvjlteue7nhtdk"} #just some random cookie number
			data_json = json.dumps(data)
			try:
				a = requests.post(url,data=data_json,headers=headers,timeout=3)
			except requests.exceptions.ReadTimeout:
				print ("We got hit with a request timeout. Restarting in 2 seconds")
				continue
			if a.status_code == 200:
				print (str(sent) + ".) The message: [" + spam + "] has been sent to victim!")
				time.sleep(0.1)
				sent += 1
			else:
				print ("Something went wrong with message: " + spam + " - idk what happened")
				print (a.status_code)
				continue
