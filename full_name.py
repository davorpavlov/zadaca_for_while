# import os

# def get_full_name(first_name: str,
#                   last_name: str,
#                   nick_name: str) -> str:
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     nick_name = nick_name.capitalize()
#     return f'{first_name} {last_name} {nick_name}'

# def get_name_parts(full_name: str):
#     name_parts = full_name.split(' ')
#     return name_parts



# first_name = input('Unesite ime: ')
# last_name = input('Unesite prezime: ')
# nick_name = input('Unesite nadimak: ')

# full_name = get_full_name(last_name=last_name,
#                           first_name=first_name,
#                           nick_name=nick_name)

# name_elements = get_name_parts(full_name)

# os.system('cls' if os.name == 'nt' else 'clear')
# print(full_name)
# print()
# for name_element in name_elements:
#     print(name_element, end='; ')

# Plan:

# 1. Učitati podatke o NBA igračima iz određenog izvora
# 2. Izračunati prosječni broj postignutih koševa svakog igrača
# 3. Sortirati igrače prema prosječnom broju postignutih koševa
# 4. Ispisati sortirane igrače

# Kod:


# koraci 1 i 2
import requests
response = requests.get('https://www.mysportsfeeds.com/api/feed/sample/pull/nba/2021-2022-regular/player_stats_totals.json')

if response.status_code == 200:
    data = response.json()['playerStatsTotals']
else:
    print('Došlo je do pogreške prilikom dohvaćanja podataka, pokušajte ponovo.')

# korak 3
sorted_players = sorted(data, key=lambda x: x['stats']['Pts']/x['stats']['GP'], reverse=True)

# korak 4
for player in sorted_players:
    print(player['player']['FirstName'], player['player']['LastName'], ' - Prosječni broj koševa po utakmici:', round(player['stats']['Pts']/player['stats']['GP'], 2))

# Napomena: Pretpostavlja se da su svi potrebni paketi već instalirani.