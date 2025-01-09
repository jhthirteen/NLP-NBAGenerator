from parse_input import extract_players, extract_statistic

def main():
    prompt = input("What would you like to find analyze? ")
    name = extract_players(prompt)
    stat = extract_statistic(prompt)

    print(name)
    print(stat)

main()