import requests

url_base = 'https://fantasy.premierleague.com/drf/bootstrap-static'
url_base_player_detail = 'https://fantasy.premierleague.com/drf/element-summary/'

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
    r = requests.get(url_base)
    for positions in r.json()['element_types']:
        print(positions['singular_name'])

def get_teams():
    r = requests.get(url_base)
    for team in r.json()['teams']:
        print(team['name'])

def get_players_details(id_element):
    r = requests.get(url_base_player_detail + id_element)
    # we have to see what data is gonna be used
    for history in r.json['history_past']:
        print(history['season_name'])


if __name__ == '__main__':
    get_players_info()