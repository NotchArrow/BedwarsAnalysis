import requests
import json
import time


def calculate_ratio(num1, num2):
	if num2 == 0:
		return num1
	else:
		return num1 / num2

def sort_dict(dictionary):
	keys = list(dictionary.keys())
	keys = sorted(keys)
	new_dictionary = {}
	for key in keys:
		new_dictionary[key] = dictionary[key]
	return new_dictionary


api_key = "[REDACTED]"
rate_limit = 300
rate_limit_refresh = 300
api_requests = 0

refresh_data = False

data = open("Data.json", "r").read()
usernames = json.loads(data)
usernames = sort_dict(usernames)
outliers = []

start_time = time.time()
for username in usernames:
	if usernames[username] == {} or refresh_data:
		# hypixel data
		r = requests.get(f'https://api.hypixel.net/player?key={api_key}&name={username}')
		
		headers = r.headers
		if (headers.get('ratelimit-remaining') == '0'):
			print("\n\n\n====================================")
			print(f"Waiting {headers.get('ratelimit-reset')}s")
			print("")
			time.sleep(float(headers.get('ratelimit-reset')) + 2)

		hypixel_user_data = json.loads(r.text)
		try:
			player_stats = hypixel_user_data['player']["stats"]
		except:
			outliers.append(username)
			continue
		try:
			bedwars_stats = player_stats["Bedwars"]
		except KeyError:
			outliers.append(username)
			continue

		# gather stats
		try: level = hypixel_user_data['player']["achievements"]["bedwars_level"]
		except KeyError: level = 0
		try: kills = bedwars_stats["kills_bedwars"]
		except KeyError: kills = 0
		try: deaths = bedwars_stats["deaths_bedwars"]
		except KeyError: deaths = 0
		try: wins = bedwars_stats["wins_bedwars"]
		except KeyError: wins = 0
		try: losses = bedwars_stats["losses_bedwars"]
		except KeyError: losses = 0
		try: final_kills = bedwars_stats["final_kills_bedwars"]
		except KeyError: final_kills = 0
		try: final_deaths = bedwars_stats["final_deaths_bedwars"]
		except KeyError: final_deaths = 0
		try: beds_broken = bedwars_stats["beds_broken_bedwars"]
		except KeyError: beds_broken = 0
		try: beds_lost = bedwars_stats["beds_lost_bedwars"]
		except KeyError: beds_lost = 0

		# calculate ratios
		kdr = round(calculate_ratio(kills, deaths), 2)
		wlr = round(calculate_ratio(wins, losses), 2)
		fkdr = round(calculate_ratio(final_kills, final_deaths), 2)
		bblr = round(calculate_ratio(beds_broken, beds_lost), 2)

		# print stats
		print()
		print(f"Username: {username}")
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

		# store all stats
		usernames[username]["level"] = level
		usernames[username]["kills"] = kills
		usernames[username]["deaths"] = deaths
		usernames[username]["kdr"] = kdr
		usernames[username]["wins"] = wins
		usernames[username]["losses"] = losses
		usernames[username]["wlr"] = wlr
		usernames[username]["final_kills"] = final_kills
		usernames[username]["final_deaths"] = final_deaths
		usernames[username]["fkdr"] = fkdr
		usernames[username]["beds_broken"] = beds_broken
		usernames[username]["beds_lost"] = beds_lost
		usernames[username]["bblr"] = bblr
	else:
		print(f"Skipped (already had stats for): {username}")

for outlier in outliers:
	usernames.pop(outlier)

file = open("Data.json", "w")
json.dump(usernames, file, indent=4)