

tic_tac_toe = """
This is the tic tac toe board

     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |

RULES
1.insert the spot number between 1 to 9
2.player one will go first
3.fill all the spot until the end of the game
4.the game end when any one of player matches their symbol either X or O
"""

spot=[' ' for i in range(9)]

attempt = 0

def reset():
    global spot,index_list
    spot = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    index_list = []
    print("xdddfsd")
    board=""" """

    

def display_board():
        
    board=f"""
     |     |
  {spot[0]}  |  {spot[1]}  |  {spot[2]}
_____|_____|_____
     |     |
  {spot[3]}  |  {spot[4]}  |  {spot[5]}
_____|_____|_____
     |     |
  {spot[6]}  |  {spot[7]}  |  {spot[8]}
     |     |

   """
    print(board)




index_list = []
def get_input(player_name):
         while True:
             while True:
                 try:
                     x = int(input(f"{player_name} enter your spot: "))
                     if type(x) == int:
                         break
                 except:
                     print("Error: please enter a number")
             x-= 1
             if 0 <= x < 9 :
                 if x in index_list:
                     print("This spot is already taken")
                 else:
                     index_list.append(x)
                     return(x)
                     break
             else:
                 print("please enter number between 1-9")

winner = 0

def game_winner(player_1,player_2):
    global winner
    if (spot[0] == spot[1] == spot[2] == 'X' or spot[3] == spot[4] == spot[5] == 'X'or

        spot[6] == spot[7] == spot[8] == 'X' or spot[0] == spot[3] == spot[6] == 'X' or

        spot[1] == spot[4] == spot[7] == 'X' or spot[2] == spot[5] == spot[8] == 'X' or
       
        spot[0] == spot[4] == spot[8] == 'X' or spot[2] == spot[4] == spot[6] == 'X'):
        
           winner+= 1
           print("Congratulations!",player_1,"you won the game! \nbetter luck next time",player_2)

           
    elif (spot[0] == spot[1] == spot[2] == 'O' or spot[3] == spot[4] == spot[5] == 'O' or

       spot[6] == spot[7] == spot[8] == 'O' or spot[0] == spot[3] == spot[6] == 'O' or

       spot[1] == spot[4] == spot[7] == 'O' or spot[2] == spot[5] == spot[8] == 'O' or
       
       spot[0] == spot[4] == spot[8] == 'O' or spot[2] == spot[4] == spot[6] == 'O'):

        winner+=1
        print("Congratulations",player_2,"you won the game \nbetter luck next time",player_1)
    
def main():
    print("Welcome to TIC TAC TOE game!")
    global player_1,player_2
    player_1 = input("player number one enter your name : ")
    player_2 = input("player number two enter your name : ")
    print("Thank you for joining\n"+player_1+"'s sign will be : X\n"+player_2+"'s sign will be : O") 

    print(tic_tac_toe)
    input("press any key to start the game:")
    display_board()

    count = 0
    for i in range(9):
        if winner == 0 :
            if i%2 == 0:
                index = get_input(player_1)
                spot[index] = 'X'
            else:
                index = get_input(player_2)
                spot[index] = 'O'
            display_board()
            game_winner(player_1,player_2)
            count+=1
    if count == 9:
        print("the game is a tie")
            
        
main()

while True:
    play_again = input("do you wanna play the game again yes/no:").lower()
    if play_again == "yes":
        winner = 0
        attempt+=1
        reset()
        main() 
    else:
        print("Thank you for joining",player_1,"and",player_2)
        break
    



     


   

    
    
    
    
        
