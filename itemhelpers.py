import json

def gainItem(item: int):
	f = open("items.json", "r")
	items = json.load(f)
	f.close()
	items["items"][item - 1] += 1
	f = open("items.json", "w")
	json.dump(items, f)
	f.close()
