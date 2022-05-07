import json
import random


# Генерация базы данных в json


db = {}
for x in range(22):
	db[f"Name {x}"] = {
		"cost":random.randint(500, 20000),
		"ower_ear":bool(random.randint(0, 1)),
		"vacuum":bool(random.randint(0, 1)),
		"down_noise":bool(random.randint(0, 1)),
		"compact":bool(random.randint(0, 1)),
		"capacity":bool(random.randint(0, 1)),
		"folding":bool(random.randint(0, 1)),
		"have_wire":bool(random.randint(0, 1)),
		"one_g":bool(random.randint(0, 1))
	}

with open("test_db.json", "w") as jfile:
	json.dump(db, jfile, indent=4)