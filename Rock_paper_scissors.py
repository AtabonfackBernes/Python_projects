import random
def play():
    user = input("Enter 'R' for rock, 'P' for Paper, or 'S' for Scissors: ")
    computer = random.choice(['R', 'P', 'S'])
    
    if user == computer:
        return "It's a Tie"
    
    if win(user,computer):
        return 'You Won!!'
    
    return 'You Lost!!'

def win(player,opponent):    
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True

print(play())

    
