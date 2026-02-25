import json
import os
import datetime

DATA_DIR = "data"

def load_json(filename, default):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=4)
        return default
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            with open(path, "w") as f:
                json.dump(default, f, indent=4)
            return default

def save_json(filename, data):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

users = load_json("users.json", {})
START_BALANCE = 1000
DAILY_AMOUNT = 500

def get_user(user_id):
    user_id = str(user_id)
    if user_id not in users:
        users[user_id] = {"balance": START_BALANCE, "last_daily": None, "times_broke":0}
        save_json("users.json", users)
    return users[user_id]

def add_balance(user_id, amount):
    user = get_user(user_id)
    user["balance"] += amount
    if user["balance"] <=0:
        user["times_broke"] = user.get("times_broke",0)+1
    save_json("users.json", users)
