#fun for tac toe table
from random import *
table =['*','*','*','*','*','*','*','*','*']
over=[]
win1=[0,1,2]
win2=[0,4,8]
win3=[0,3,6]
win4=[2,5,8]
win5=[2,4,6]
win6=[6,7,8]
player1_list=[]
player2_list=[]
player=randint(1,2)
print("Players will be generated randomly (Play accordingly)")

if player==1:
    print("Player 1:X")
    print("Player 2:0")
    player1='X'
    player2='0'
else:
    print("Player 1:0")
    print("Player 2:X")
    player1='0'
    player2='X'

#function to display the tic_tac_toe board
def show_table():
    for i in range(1,10):
        print(table[i-1],end="")
        
        if(i%3==0 and i!=9):
            print("\n_________")
        else:
            if i!=9:
                print(" | ",end="")
            else:
                pass
show_table()
print("\n\n.....|| THE GAME BEGINS ||.....")
#function to check the winner
def winner():
    if player1_list==win1 or player1_list==win2 or player1_list==win3 or player1_list==win4 or player1_list==win5 or player1_list==win6:
        print("\n     Player 1 won the match\n     Player 2 better luck next time")
        exit()
    if player2_list==win1 or player2_list==win2 or player2_list==win3 or player2_list==win4 or player2_list==win5 or player2_list==win6:
        print("\n     Player 2 won the match\n     Player 1 better luck next time")
        exit()

#function to get input from the user with validation
def userinput():
    for j in range(1,10):
        num=0
        if j%2==0:
            print("\nPlayer 2 turn>>")
            while num not in range(1,10):
                num=int(input("Enter the postion (1 to 9)>>"))
                if num-1 in over:
                    print(table[num-1]+"Already exits\nEnter valid number")
                    show_table()
                    num=0
            over.append(num-1)
            player2_list.append(num-1)
            player2_list.sort()
            table[num-1]=player2
            show_table()
        else:
            print("\nPlayer 1 turn>>")
            while num not in range(1,10):
                num=int(input("Enter the postion (1 to 9)>>"))
                if num-1 in over:
                    print(table[num-1]+" Already exits\nEnter valid number\n")
                    show_table()
                    num=0
                
            over.append(num-1)
            player1_list.append(num-1)
            player1_list.sort()
            table[num-1]=player1
            show_table()
        if j>4:
            winner()
userinput()


