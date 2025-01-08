import requests
from bs4 import BeautifulSoup

"""
NOTE: Rate limit of 20 requests per limit
"""

def build_player_url(name):
    base_url = 'https://www.basketball-reference.com/players'
    first_letter_last_name_pos = name.rfind(' ') + 1 #Makes the assumption that the first and last name are space delimited

    try:
        index_letter = name[first_letter_last_name_pos].lower() 
    except:
        print("Input Error: Name of player could not be processed")
        exit()
    
    if( len(name[first_letter_last_name_pos:len(name)]) <= 5 ):
        base_url += f"/{index_letter}/{name[first_letter_last_name_pos:len(name)].lower()}{name[0:2].lower()}01.html"
    else:
        base_url += f"/{index_letter}/{name[first_letter_last_name_pos:first_letter_last_name_pos+5].lower()}{name[0:2].lower()}01.html"
    print(base_url)
    return base_url

def fetch_player_data_html(url):
    r = requests.get(url)
    if( r.status_code != 200 ): #200 --> indicative of a successful GET request
        print(f"Bad Request Error: {r.status_code}")
        exit()
    
    return r.text

def fetch_player_game_log_html(player_base_url, year):
    url_cutoff_position = player_base_url.rfind('.')
    game_log_url = f"{player_base_url[0:url_cutoff_position]}/gamelog/{year}"
    r = requests.get(game_log_url)
    if( r.status_code != 200 ): #200 --> indicative of a successful GET request
        print(f"Bad Request Error: {r.status_code}")
        exit()
    
    return r.text

def fetch_player_game_log(name, year):
    url = build_player_url(name)
    player_data_html = fetch_player_game_log_html(url, year)
    parser = BeautifulSoup(player_data_html, "html.parser")
    game_log_table = parser.find("table", {"id" : "pgl_basic"}) #table ID on a player's game log
    if( game_log_table == None ):
        print("Parsing Error: Game Log Table not Found")
        exit()
    
    game_log_headers = game_log_table.find("thead").find_all("th")
    return game_log_headers

def main():
    #fetch_player_game_log("Jayson Tatum", 2025)
    build_player_url("De'Aron Fox")


main()