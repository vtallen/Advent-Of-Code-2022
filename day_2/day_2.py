strategy_guide_file = open("startegy_guide.txt", "r")
strategy_guide = strategy_guide_file.readlines()
strategy_guide_file.close()

#A dictionary that holds every case that could happen with the normal game of rock paper scissors
#In part one
rules = {
    #The values of each choice. Rock: A, Paper:B, Scissors: C
    "A": 1,
    "B": 2,
    "C": 3,

    "X": 1,
    "Y": 2,
    "Z": 3,
}

#Based on the line read from the strategy_guide.txt, we get the correct choice
correct_choice = {
    "A X": "C",
    "A Y": "A",
    "A Z": "B",

    "B X": "A",
    "B Y": "B",
    "B Z": "C",

    "C X": "B",
    "C Y": "C",
    "C Z": "A",
}

player_score = 0
opponent_score = 0

#These are the scores awarded for a lose, tie, and win
lose_score = 0
tie_score = 3
win_score = 6

round_num = 1

for line in strategy_guide:
    print("Round", round_num)

    line = line.strip("\n")
    plays = line.split(" ")

    opponent_choice = plays[0]
    player_strategy = plays[1]

    print("Opponent Choice:", opponent_choice)

    player_choice = correct_choice.get(line)
    print("Correct Choice from the strategy guide:", player_choice)

    #The line read from strategy guide corrected with the proper choice
    new_line = opponent_choice + " " + player_choice

    opponent_choice_score = rules.get(opponent_choice)
    player_choice_score = rules.get(player_choice)

    #Add the value of the opponent's choice to their score
    opponent_score += opponent_choice_score


    #Add the value of your choice to your score
    player_score += player_choice_score

    #checks if there is a tie
    if opponent_choice == player_choice:
        print("Tie")
        opponent_score += tie_score

        player_score += tie_score

    else:
        winner = rules.get(new_line)

        if winner == "opponent":
            print("Winner: opponent")
            opponent_score += win_score
        elif winner == "player":
            print("Winner: player")
            player_score += win_score

    print("")
    round_num += 1



print("Opponent Score:", opponent_score)
print("Player Score", player_score)





