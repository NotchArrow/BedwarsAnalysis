import json


data = open("Data.json", "r").read()
usernames = json.loads(data)


level = 0
kills = 0
deaths = 0
wins = 0
losses = 0
final_kills = 0
final_deaths = 0
beds_broken = 0
beds_lost = 0


for username in usernames:
	level += usernames[username]["level"]
	kills += usernames[username]["kills"]
	deaths += usernames[username]["deaths"]
	wins += usernames[username]["wins"]
	losses += usernames[username]["losses"]
	final_kills += usernames[username]["final_kills"]
	final_deaths += usernames[username]["final_deaths"]
	beds_broken += usernames[username]["beds_broken"]
	beds_lost += usernames[username]["beds_lost"]


kdr = round(kills / deaths, 2)
wlr = round(wins / losses, 2)
fkdr = round(final_kills / final_deaths, 2)
bblr = round(beds_broken / beds_lost, 2)


print("Totals/Averages:")
print(f"Players: {len(usernames)}")
print(f"Level: {level}")
print(f"Kills: {kills}")
print(f"Deaths: {deaths}")
print(f"KDR: {kdr}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"WLR: {wlr}")
print(f"Final Kills: {final_kills}")
print(f"Final Deaths: {final_deaths}")
print(f"FKDR: {fkdr}")
print(f"Beds Broken: {beds_broken}")
print(f"Beds Lost: {beds_lost}")
print(f"BBLR: {bblr}")
print(final_kills / level)