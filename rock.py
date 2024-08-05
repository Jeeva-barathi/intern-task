import random
def play():
    player=str(input("r for ROCK,p for PAPER,s for scissors:")).lower()
    choose=["r","p","s"]
    computer=random.choice(choose)
    print(f'your choice{player} <=> opponent{computer}')
    if(player==computer):
        print("game is in tie")
    elif((player=='r' and computer=='s') or 
         (player=='p' and computer=='r') or
         (player=='s' and computer=='p')):
        print("you won the game")
    else:
        print("good try better luck next time")
play()