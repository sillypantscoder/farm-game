import json

def gainItem(item: str):
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	items["items"][item] += 1
	f = open("items.json", "w")
	json.dump(items, f)
	f.close()

def loseItem(item: str):
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	items["items"][item] -= 1
	f = open("items.json", "w")
	json.dump(items, f)
	f.close()

def getItems():
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	return items["items"]

def getItem(item: str):
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	return items["items"][item]

def getMoney():
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	return items["money"]

def setMoney(money: int):
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	items["money"] = money
	f = open("items.json", "w")
	json.dump(items, f)
	f.close()
