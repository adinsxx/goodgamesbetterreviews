import requests
import webbrowser
import json



url = "https://id.twitch.tv/oauth2/token?client_id=zfhmt4lt50bo48lpv9g3hzgspq9ex9&client_secret=7as9vugu0p4ikcn9k9j8kwm688ltyj&grant_type=client_credentials"

response = requests.post(url)

clientID = "zfhmt4lt50bo48lpv9g3hzgspq9ex9"
accessToken = "0j7ac2oe7s63wxfpubkpxuowr97z7v"
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     accessToken = data["access_token"]
#     print(accessToken)
# else:
#     print("request failed")

games_url = 'https://api.igdb.com/v4/games/'
art_url = 'https://api.igdb.com/v4/artworks'
generic_header = {'Client-ID': '{}'.format(clientID),'Authorization': 'Bearer {}'.format(accessToken)}

search_input = input("type the name of a game: ")
search_body = 'search "{}"; fields name, cover.url;'.format(search_input)
selected_data = ''
search_response = requests.post(games_url,headers=generic_header,data=search_body)
search_data = search_response.json()
for item in search_data:
    user_select = input('Do you want: {}?\n>>>'.format(item['name']))
    if (user_select == "yes") or (user_select == "y"):
        selected_data = item
        break
if selected_data != '':
    if 'cover' in selected_data:
        cover = selected_data.get('cover')
        cover = cover.get('url')
        cover = cover.replace("thumb","1080p")
        webbrowser.open_new_tab(cover)
    else:
        print("no cover????")
else:
    print('You have to select something')
