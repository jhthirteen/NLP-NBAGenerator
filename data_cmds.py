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
    
    if( len(name[first_letter_last_name_pos:len(name)]) <= 5 ): #case --> last name is less than or equal to 5 characters long 
        base_url += f"/{index_letter}/{name[first_letter_last_name_pos:len(name)].lower()}{name[0:2].lower()}01.html"
    else: #case --> last name is longer than 5 characters 
        base_url += f"/{index_letter}/{name[first_letter_last_name_pos:first_letter_last_name_pos+5].lower()}{name[0:2].lower()}01.html"
    
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
    
    game_log_rows = game_log_table.find("tbody").find_all("tr")
    return game_log_rows

def fetch_three_point_percentage_last_games(game_log, num_games):
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()
    
    three_point_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    index = len(game_log) - 1 #allows us to index into the back of the game log (where the most recent games are stored)
    for i in range(num_games):
        three_point_percentage = game_log[index].find("td", {"data-stat" : "fg3_pct"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        three_point_data[i] = three_point_percentage.text #populate the data array with the percentage 
        index -= 1

    return three_point_data

def main():
    log_rows = fetch_player_game_log("Shai Gilgeous-Alexander", 2025)
    fetch_three_point_percentage_last_games(log_rows, 5)



main()