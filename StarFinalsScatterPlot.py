import json
import matplotlib.pyplot


data = open("Data.json", "r").read()
usernames = json.loads(data)

stars = []
finals = []

for username in usernames:
	stars.append(usernames[username]["level"])
	finals.append(usernames[username]["final_kills"])

matplotlib.pyplot.scatter(stars, finals, marker=".", s=25)
matplotlib.pyplot.xlabel("Stars")
matplotlib.pyplot.ylabel("Final Kills")
matplotlib.pyplot.title("Bedwars Stars to Finals")
matplotlib.pyplot.show()