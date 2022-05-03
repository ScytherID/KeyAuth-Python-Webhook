from multiprocessing.sharedctypes import Value
from turtle import color
from unicodedata import name
from urllib import response
from keyauth import api
from discord_webhook import DiscordWebhook , DiscordEmbed
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime

print("Connect to Server KeyAuth.win")
def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
    	path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest
keyauthapp = api(
	name = "",
	ownerid = "",
	secret = "",
	version = "1.0",
	hash_to_check = getchecksum()
)
sleep(1.5) 
print(f"Login Status : {keyauthapp.check()}")
sleep(1.5) 
print(f"Checking Hwid Ban? : {keyauthapp.checkblacklist()}") 
if keyauthapp.checkblacklist() == True:
	print("You got hwid ban:( ")
	print("So sad go use hwid spoofer xd")
	contentss = "Warning Ban user try to login Tools!!" 
	webhooks = DiscordWebhook(url="Your Webhook", username="Name Webhook", content=contentss)
	webhooks.execute()
	sleep(1.5)
	exit(0)

sleep(1.5)
print ("Do you want login (y/n) ?")
loginid=input("Choice please: ") 
if loginid=="y": 
	user = input('Username: ')
	password = input('Password: ')
	keyauthapp.login(user,password)
elif loginid=="n":
	print("Cencel Login!") 
	sys.exit()

usernameid = "Username : " + keyauthapp.user_data.username + "\n" + "Ip : " + keyauthapp.user_data.ip + "\n" + "Hwid : " + keyauthapp.user_data.hwid 
print(f"Login Status: {keyauthapp.check()}")
webhook = DiscordWebhook(url="Your Webhook", username="Name Webhook", content=usernameid)
response = webhook.execute()
print("Exit Tools...")
sleep(10)
exit(0)
