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

def fetch_three_point_attempts_last_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()
    
    games_found = 0
    three_point_attempt_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    index = len(game_log) - 1 #allows us to index into the back of the game log (where the most recent games are stored)
    while( games_found < num_games ):
        three_point_attempts = game_log[index].find("td", {"data-stat" : "fg3a"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( three_point_attempts ):
            three_point_attempt_data[games_found] = three_point_attempts.text #populate the data array with the percentage 
            games_found += 1
        index -= 1

    return three_point_attempt_data

def fetch_three_point_attempts_first_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()

    games_found = 0 
    three_point_attempt_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    while( games_found < num_games ):
        three_point_attempts = game_log[games_found].find("td", {"data-stat" : "fg3a"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( three_point_attempts ):
            three_point_attempt_data[games_found] = three_point_attempts.text #populate the data array with the percentage 
            games_found += 1

    return three_point_attempt_data 

def fetch_three_point_percentage_last_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()
    
    games_found = 0
    three_point_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    index = len(game_log) - 1 #allows us to index into the back of the game log (where the most recent games are stored)
    while( games_found < num_games ):
        three_point_percentage = game_log[index].find("td", {"data-stat" : "fg3_pct"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( three_point_percentage ):
            three_point_data[games_found] = three_point_percentage.text #populate the data array with the percentage 
            games_found += 1
        index -= 1

    return three_point_data

def fetch_three_point_percentage_first_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()

    games_found = 0 
    three_point_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    while( games_found < num_games ):
        three_point_percentage = game_log[games_found].find("td", {"data-stat" : "fg3_pct"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( three_point_percentage ):
            three_point_data[games_found] = three_point_percentage.text #populate the data array with the percentage 
            games_found += 1

    return three_point_data  

def fetch_fieldgoal_point_percentage_last_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()
    
    games_found = 0
    fg_point_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    index = len(game_log) - 1 #allows us to index into the back of the game log (where the most recent games are stored)
    while( games_found < num_games ):
        fg_point_percentage = game_log[index].find("td", {"data-stat" : "fg_pct"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( fg_point_percentage ):
            fg_point_data[games_found] = fg_point_percentage.text #populate the data array with the percentage 
            games_found += 1
        index -= 1

    return fg_point_data

def fetch_fieldgoal_point_percentage_first_games(name, num_games, year):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()

    games_found = 0 
    fg_point_data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    while( games_found < num_games ):
        fg_point_percentage = game_log[games_found].find("td", {"data-stat" : "fg_pct"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( fg_point_percentage ):
            fg_point_data[games_found] = fg_point_percentage.text #populate the data array with the percentage 
            games_found += 1

    return fg_point_data     


# ATTEMPT AT SINGLE, ABSTRACTED VERSIONS OF THE LAST n GAMES AND FIRST n GAMES BELOW
#NOTE: stat paramater should be passed in the format of the HTML element we are searching for --> for example, stat = "fg_pct"
# we want to have the OpenAI API format this for us 

def fetch_stat_first_games(name, num_games, year, stat):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()

    games_found = 0 
    data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    while( games_found < num_games ):
        stats = game_log[games_found].find("td", {"data-stat" : f"{stat}"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( stats ):
            data[games_found] = stats.text #populate the data array with the percentage 
            games_found += 1

    return data 

def fetch_stat_last_games(name, num_games, year, stat):
    game_log = fetch_player_game_log(name, year)
    if( num_games > len(game_log) - 1):
        print("Input Error: Number of games searched for exceeds the number of games played by player")
        exit()
    
    games_found = 0
    data = [None] * num_games #allocate the space needed to store the data the number of percentages we are holding
    index = len(game_log) - 1 #allows us to index into the back of the game log (where the most recent games are stored)
    while( games_found < num_games ):
        stats = game_log[index].find("td", {"data-stat" : f"{stat}"}) #find the <td> element containing the three point percentage for the game specified by the current row 
        if( stats ):
            data[games_found] = stats.text #populate the data array with the percentage 
            games_found += 1
        index -= 1

    return data

"""
TODO: Add a function that allows a user to search for three point percentages within a specified range of dates
Idea here --> prompt the user that the player had at least one inactive game during this stretch --> prompt them if we would like the
past 5 games that THEY played, or the past 5 games the team played (including some inactive games in that case)
TODO: These functions can all be generalized to a single function with the data-stat tag being matched up with via some mapping at the beginning of the function.
"""

def main():
    log_rows = fetch_player_game_log("Shai Gilgeous-Alexander", 2025)
    #fetch_three_point_percentage_last_games(log_rows, 5)



main()