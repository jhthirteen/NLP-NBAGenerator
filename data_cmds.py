import requests
from bs4 import BeautifulSoup

def build_player_url(name):
    base_url = 'https://www.basketball-reference.com/players'
    first_letter_last_name_pos = name.rfind(' ') + 1 #Makes the assumption that the first and last name are space delimited

    try:
        index_letter = name[first_letter_last_name_pos].lower()
    except:
        print("Input Error: Name of player could not be processed")
        exit()
    
    base_url += f"/{index_letter}/{name[first_letter_last_name_pos:len(name)].lower()}{name[0:2].lower()}01.html"
    return base_url

def fetch_player_data(name):
    url = build_player_url(name)
    r = requests.get(url)
    if( r.status_code != 200 ): #200 --> indicative of a successful GET request
        print(f"Bad Request Error: {r.status_code}")
        exit()
    
    print(r.text)

def main():
    print("hello world")
    fetch_player_data("Tyrese Maxey")

main()