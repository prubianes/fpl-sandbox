import requests

def get_players_info():
    url = 'https://fantasy.premierleague.com/drf/bootstrap-static'
    r = requests.get(url)
    for player in r.json()['elements']:
        print('---------------- \r')
        print(player['element_type'])
        print(player['code'])
        print(player['team_code'])
        print(player['first_name'] + ' ' + player['second_name'])
        print(player['now_cost'])

if __name__ == '__main__':
    get_players_info()