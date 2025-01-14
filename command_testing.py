from data_cmds import fetch_three_point_percentage_last_games, fetch_player_game_log

player = "LaMelo Ball" #had an inactive stretch recently
l = fetch_player_game_log(player, 2025)
num_games = 5
data = [None] * num_games

back_index = len(l) - 1
games_found = 0

while( games_found < num_games ):
    r = l[back_index].find("td", {"data-stat" : "fg3_pct"})
    if( r ):
        data[games_found] = r.text
        games_found += 1
    back_index -= 1

print(data)
