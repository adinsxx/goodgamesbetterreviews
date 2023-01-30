import json
from difflib import get_close_matches

user_search_input = "Doom Eternal"

steamgames_link = "games_stripped_down.json"

with open(steamgames_link, "r") as file:
    gamedata = json.load(file)

appid_list, name_list = zip(*gamedata)
print(appid_list)

#print(get_close_matches(user_search_input,gamedata[1]))