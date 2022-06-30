import requests
from pprint import pprint
# response = requests.get("https://superheroapi.com/api/2619421814940190/search/Captain America")
# # pprint(response)
# pprint(response.text)
# # pprint(response.content)
# r = requests.get("https://superheroapi.com/api/2619421814940190/332/powerstats")
# s = r.json()
# print(s['intelligence'])

heroes_list = [
    {'name': 'Hulk'},
    {'name': 'Captain America'},
    {'name': 'Thanos'}
]

for person in heroes_list:
    # print(person['name'])
    url = "https://superheroapi.com/api/2619421814940190/search/"
    url = url + person['name']
    # print(url)
    response = requests.get(url)
    dict = response.json()
    person['intelligence'] = int(dict['results'][0]['powerstats']['intelligence'])

# pprint(heroes_list)

sorted_heroes_list = sorted(heroes_list, key = lambda k: k ['intelligence'])
pprint(sorted_heroes_list[-1]['name'])