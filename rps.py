choice = ["rock","paper","sissors"]

# input the choices in valid words and it will tell you who won
def rpsWords(choiceP1,choiceP2):
    print("\n" + choiceP1 +" vs "+  choiceP2)
    if (choiceP1 == choiceP2): return("draw")
    p1,p2 = choice.index(choiceP1),choice.index(choiceP2)
    for i in range(3): #loop checks if neither player got rock, then paper, then sissors
        if (p1 != i and p2 != i):
            winningChoice = choice[i-1] # it knows what won, but not who won
            if (choiceP1 == winningChoice): return "P1 wins: " + whoWon(choiceP1,choiceP2)
            else: return "P2 wins: " + whoWon(choiceP2,choiceP1)

#knows what won but not who won
def rps(p1,p2):
    if (p1 == p2): return("draw")
    for i in range(3):
        if (p1 != i and p2 != i): return(choice[i-1] + " wins!")
            
def whoWon(winner,loser):
    return winner + " beats " + loser

# testing to see if it works
for p1 in choice:
    for p2 in choice:
        print(rpsWords(p1,p2))
