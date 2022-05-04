from multiprocessing.sharedctypes import Value
from nturl2path import url2pathname
from tkinter import Y
from turtle import color
from unicodedata import name
from urllib import response
import discord_webhook
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
os.system("cls")
sleep(1.5)
print("Success Connect To Server.")
sleep(1.5) 
keyauthapp.checkblacklist() 
if keyauthapp.checkblacklist() == True:
    keyauthapp.check()
    keyauthapp.ban()
    print("YOUR HWID & IP GOT BANNED.")
    print("IF YOU DO NOT EXIT THE PROGRAM THAN 3 TIMES, YOU WILL BE ENTERED TO THE SERVER LIST!")
    webhookban = DiscordWebhook(url='Webhook')
    embedban = DiscordEmbed(title='BAN USERS - BOT', description="USERS BAN TRY TO LOGIN\n" + "WARNING.", color='03b2f8')
    webhookban.add_embed(embedban)
    response = webhookban.execute()
    EXIT = input("Press Enter To Exit.")
    exit(0)
        
     
keyauthapp.check()
sleep(1.5) 
os.system("cls")
user = input('Username: ')
password = input('Password: ')
keyauthapp.login(user,password)
keyauthapp.check()
webhookinfo = DiscordWebhook(url='Webhook')
embed = DiscordEmbed(title='KEY INFO - BOT', description="User  :   " + keyauthapp.user_data.username + "\nIp  :   " + keyauthapp.user_data.ip + "\n Hwid  :   " + keyauthapp.user_data.hwid + "\nOnline Users : " + keyauthapp.app_data.numUsers + "\nUSERS HAS LOGIN.", color='03b2f8')
webhookinfo.add_embed(embed)
response = webhookinfo.execute()
"""
Your code python :D
"""
input('Press Enter to exit.')
