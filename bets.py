from economy import save_json, get_user
import json
import os

DATA_DIR = "data"
bets_data = load_json("bets.json", {"bet_counter":1,"bets":{}})

def save_bets():
    save_json("bets.json", bets_data)

def create_bet(name, options, creator_id):
    bet_id = bets_data["bet_counter"]
    bets_data["bets"][str(bet_id)] = {
        "name": name,
        "options": options,
        "creator": str(creator_id),
        "bets": {},
        "resolved": False
    }
    bets_data["bet_counter"] +=1
    save_bets()
    return bet_id

def place_bet(bet_id, user_id, option, amount):
    bid = str(bet_id)
    bet = bets_data["bets"][bid]
    user = get_user(user_id)
    user["balance"] -= amount
    if user["balance"]==0:
        user["times_broke"] = user.get("times_broke",0)+1
    bet["bets"][str(user_id)] = {"option": option, "amount": amount}
    save_bets()

def resolve_bet(bet_id, correct_option):
    bid = str(bet_id)
    bet = bets_data["bets"][bid]
    winners=[]
    losers=[]
    top_bets=[]
    for user_id, bdata in bet["bets"].items():
        amount = bdata["amount"]
        option = bdata["option"]
        top_bets.append((amount,user_id))
        if option == correct_option:
            payout = amount*2
            get_user(user_id)["balance"] += payout
            winners.append(f"<@{user_id}> +{payout}")
        else:
            losers.append(f"<@{user_id}> lost {amount}")
    bet["resolved"] = True
    save_bets()
    top_bets.sort(reverse=True)
    top3 = "\n".join([f"<@{uid}>: {amt} on {bet['name']}" for amt,uid in top_bets[:3]])
    return winners, losers, top3
