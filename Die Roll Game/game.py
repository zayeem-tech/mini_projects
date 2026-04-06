import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input('Enter the number of players(2-4): ')
    if players.isdigit():
        players = int(players)
        if players > 1 and players < 5:
            break
        else:
            print(' Please enter a number between 2 and 4.')
    else:
        print(' Please enter a number.')

max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f' Player {player_idx + 1}\'s turn has just started.')
        print(f' Your total score is {player_scores[player_idx]}')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y/n)? ')
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print(' You rolled a 1. Your turn is done.')
                current_score = 0
                break
            else:
                current_score += value
                print(f'\n You rolled a {value}.')
            print(f'\n Your score is {current_score}')
            
        player_scores[player_idx] = current_score
        print(f'\n Your total score is {player_scores[player_idx]}')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f'\n Player number {winning_idx + 1} is the winner with a score of {max_score}.')