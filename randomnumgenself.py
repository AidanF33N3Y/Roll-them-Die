import random

def roll():
    use = random.randint(1,6)
    return use

max_score_input = input('Please First input the score you want to play until: ')
if max_score_input.isdigit():
    max_score_input = int(max_score_input)
else:
    print("You must input a number")

while True:
    player_number_input = input("Input Player Number Amount (2-4) ")
    if player_number_input.isdigit():
        player_number_input = int(player_number_input)
        if 2 <= player_number_input <=4:
            break
        else:
            print("You must choose between 2 and 4")
    else:
        print("You Must Input A Valid Input")        

print(f"Playing until a score of {max_score_input}")

def playloop():
    
    count_moves = 0
    print(f'Once the score is equal to {max_score_input} the game will terminate')

    player_scores = [0 for _ in range(player_number_input)]
    player_moves = [0 for _ in range(player_number_input)]
    print(player_scores)
    while max(player_scores) < max_score_input:
        for player_idx in range(player_number_input):
            
            while max_score_input >= player_scores[player_idx]:
                check = input(f'Player {player_idx + 1} Press Y to roll: ' )
                
                if check.lower() == 'y':
                    print("Rolling!!")
                    rolled_value = roll()
                    if 2 <= rolled_value <= 6:
                        player_scores[player_idx] += rolled_value
                        player_moves[player_idx] += 1
                        print(f"2-6 {rolled_value} {player_scores[player_idx]}")
                        
                    else:
                        player_scores[player_idx] += rolled_value
                        player_moves[player_idx] += 1
                        print(f'1 {player_scores[player_idx]}')
                        
                else:
                    print("Read Above and Run Again")
            if player_scores[player_idx] >= max_score_input - 1:
                player_scores.append(player_idx)
                player_moves.append(count_moves)
                player_moves.pop()
                print(f'Player {player_idx + 1} had a score of {player_scores[player_idx]} and {player_moves[player_idx]} moves')
                print(f'{player_moves}')

    winner_idx = player_moves.index(min(player_moves))
    print(f"Player {winner_idx + 1} wins with a move total of {min(player_moves)} moves")
    loser_idx = player_moves.index(max(player_moves))
    print(f"Player {loser_idx + 1} loses with a move total of {max(player_moves)} moves")
                


playloop()
