import json

def grab_usernames():
	data = open("Data.json", "r").read()
	current_usernames = json.loads(data)

	log_file = open("C:/Users/*****/curseforge/minecraft/Instances/PvP/logs/latest.log", "r")
	log_file_lines = log_file.readlines()

	usernames = []
	for line in log_file_lines:
		if "[CHAT]" in line:
			line = line.split("[CHAT]")[1]
			if "ONLINE: " in line:
				line = line.strip()
				line = line.replace("ONLINE: ", "")
				usernames += line.split(", ")
			elif "Online Players" in line:
				line = line.split(": ")[1]
				line = line.split(", ")
				for username in line:
					username = username.replace("[MVP++] ", "")
					username = username.replace("[MVP+] ", "")
					username = username.replace("[MVP] ", "")
					username = username.replace("[VIP+] ", "")
					username = username.replace("[VIP] ", "")
					username = username.strip()
					usernames.append(username)
			elif "joined the lobby!" in line:
				line = line.split("joined the lobby!")[0]
				line = line.split("] ")[1]
				line = line[:-5]
				usernames.append(line)

	new_usernames = 0
	for username in usernames:
		if username not in current_usernames:
			current_usernames[username] = {}
			new_usernames += 1

	file = open("Data.json", "w")
	json.dump(current_usernames, file, indent=4)


	print(f"New Usernames: {new_usernames}")
	print(f"Total Usernames: {len(current_usernames)}")

if __name__ == "__main__":
	grab_usernames()