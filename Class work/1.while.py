moves=34
winningpoint=int(input("Enter the winningpoint: "))

while moves>0:
    if moves == winningpoint:
        print("Congrats, You won!!")
        break
    print(f"{moves} are left. You have chance to win the game!!")
    moves-=1
else:
    print("Game Over!!!")