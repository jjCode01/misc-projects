import random

if __name__ == "__main__":
    num_of_players = 1000
    players = [1] * num_of_players
    for flip in range(10):
        if sum(players) <= 1:
            break
        for i, player in enumerate(players):
            if player:
                players[i] = random.choice([0, 1])
        print(f"Flip #{flip + 1}: {sum(players):,} remaining")

    winners = [i for i, player in enumerate(players) if player == 1]
    if not winners:
        print("No Winners :(")
    else:
        print(f"{sum(players)} Winner{'s' if sum(players) > 1 else ''}: {winners}")
