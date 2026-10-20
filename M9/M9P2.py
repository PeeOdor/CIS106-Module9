# Problem 2 - Batting average with a function

def compute_batting_avg(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats


player_count = 0
response = "Y"

while response.upper() == "Y":
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    avg = compute_batting_avg(hits, at_bats)
    player_count += 1

    print(f"Player: {last_name}  Batting Average: {avg:.3f}")

    response = input("Enter another player? (Y/N): ")

print(f"\nNumber of players entered: {player_count}")