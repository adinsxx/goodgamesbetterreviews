import requests
import webbrowser
import json



url = "https://id.twitch.tv/oauth2/token?client_id=zfhmt4lt50bo48lpv9g3hzgspq9ex9&client_secret=7as9vugu0p4ikcn9k9j8kwm688ltyj&grant_type=client_credentials"

response = requests.post(url)

accessToken = "rfnm4avg7vp3qfyrpizyzyc05gfsnz"
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

search_input = 'doom 64'
search_body = 'search "{}"; fields name, cover.url;'.format(search_input)

search_response = requests.post(games_url,headers=generic_header,data=search_body)
search_data = search_response.json()
for item in search_data:
    cover = item.get('cover')
    cover = cover.get('url')
    cover = cover.replace("thumb","1080p")
    webbrowser.open_new_tab(cover)