import requests
import webbrowser
import json



url = "https://id.twitch.tv/oauth2/token?client_id=zfhmt4lt50bo48lpv9g3hzgspq9ex9&client_secret=7as9vugu0p4ikcn9k9j8kwm688ltyj&grant_type=client_credentials"

response = requests.post(url)

accessToken = "ajjvirzt6utqyi99sxprbndsdip7us"
clientID = "zfhmt4lt50bo48lpv9g3hzgspq9ex9"

# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     accessToken = "Bearer " + data["access_token"]
# else:
#     print("request failed")

games_url = 'https://api.igdb.com/v4/games/'
art_url = 'https://api.igdb.com/v4/artworks'
generic_header = {'Client-ID': '{}'.format(clientID),'Authorization': 'Bearer {}'.format(accessToken)}

search_input = 'crash bandicoot'
search_body = 'search "{}"; fields name, artworks;'.format(search_input)

search_response = requests.post(games_url,headers=generic_header,data=search_body)
search_data = search_response.json()
json_formatted_str = json.dumps(search_data, indent=4)
print(json_formatted_str)
art_urls = {}
for game in search_data:
    print(game)
    if 'artworks' in game:
        print(game['artworks'])
    else:
        print('No art :(')