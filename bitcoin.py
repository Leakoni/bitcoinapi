import requests
import json
from os import system
import threading
from datetime import datetime
import random

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
usdsek = requests.get("https://www.freeforexapi.com/api/live?pairs=USDSEK")
rate_usdsek = usdsek.json()["rates"]["USDSEK"]["rate"]


json = response.json()["bpi"]["USD"]

def bitcoin(code, rate):
	system("clear")
	print(code + " - SEK")
	rate = round(rate,2)
	sek = rate * rate_usdsek
	sek = round(sek,2)
	print(str(rate) + "$ - " + str(sek) + " KR")
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Last Updated: " + current_time)

def app():
	update = random.uniform(1.0,20.0)
	threading.Timer(update, app).start()
	bitcoin(json["code"], json["rate_float"])

app()
