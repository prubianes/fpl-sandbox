import requests

url_base = 'https://fantasy.premierleague.com/drf/bootstrap-static'

def get_players_info():
    r = requests.get(url_base)
    for player in r.json()['elements']:
        print('---------------- \r')
        print(player['element_type'])
        print(player['code'])
        print(player['team_code'])
        print(player['first_name'] + ' ' + player['second_name'])
        print(player['now_cost'])

def get_positions():
    r = requests.get(url)
    for positions in r.json()['element_types']:
        print(positions['singular_name'])


if __name__ == '__main__':
    get_players_info()