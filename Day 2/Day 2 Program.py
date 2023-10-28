f = open("Day 2 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

games = fileinput.splitlines()

score = 0

for i in games: #Loops through all the games
    moves = i.split(" ")
    score += (ord(moves[1]) - 87) #X is 88, Y is 89, Z is 90. This gives the correct score for the move you pick

    #These 2 lines give each player a zero if they play rock, 1 for paper and 2 for scissors
    opponent = ord(moves[0]) - 65 #A is 65, B is 66, C is 67

    you = ord(moves[1]) - 88



    if opponent == you:
        score += 3 #3 points for a draw


    #If you have one ascii value higher than the opponent (or 2 for scissors vs 0 against rock), you win and get 6 points
    elif (you - opponent) % 3 == 1:
        score += 6
    

print(score)

#Day 2


score = 0


for i in games:
    moves = i.split(" ")

    if moves[1] == "Y":
        score += 3 + ord(moves[0]) - 64

    elif moves[1] == "X":
        score += ((ord(moves[0]) - 65 - 1) % 3) + 1

    else:
        score += 6 + ((ord(moves[0]) - 65 + 1) % 3) + 1


print(score)







