import requests
import json

url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data from URL")

applist = data["applist"]["apps"]
print(len(applist))

output = []
for app in applist:
    if (not app["name"] == ""):
        appid = app["appid"]
        name = app["name"]
        output.append({"appid": appid, "name": name})

with open('games_stripped_down.json', 'w') as file:
    json.dump(output, file, indent=4)