import csv
def main():
    file_path = "wimbledon.csv"

    data = read_csv(file_path)

    wins_dictionary = count_wins(data)

    display_champions_wins(wins_dictionary)

    countries_list = list_countries(data)

    display_countries(countries_list)
def read_csv(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            data.append(row)
    return data

def count_wins(data):
    wins_dict = {}
    for row in data[1:]:  # Skip the header row
        champion = row[0]
        wins = int(row[1]) if row[1].isdigit() else 0
        wins_dict[champion] = wins_dict.get(champion, 0) + wins
    return wins_dict



def list_countries(data):
    countries_set = set(row[2] for row in data)
    return sorted(countries_set)

def display_champions_wins(wins_dict):
    print("Wimbledon Champions:")
    for champion, wins in wins_dict.items():
        print(f"{champion} {wins}")

def display_countries(countries_list):
    print("\nThese countries have won Wimbledon:")
    countries_str = ', '.join(countries_list)
    print(countries_str)

main()
