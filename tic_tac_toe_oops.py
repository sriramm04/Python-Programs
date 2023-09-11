
class game:
    def __init__(self):

        self.winner = 0
        self.spot = []
        self.spot = [' ' for i in range(9)]
        self.attempt = 0
        self.index_list = []
        
    def reset(self):
         #board =f""
            self.index_list = []
            self.spot = []
            self.spot = [' ' for i in range(9)]
            print("second time")
        
        

    def display_board(self):
        if self.attempt == 1:
            self.attempt+=1
            self.reset()

        board=f"""
     |     |
  {self.spot[0]}  |  {self.spot[1]}  |  {self.spot[2]}
_____|_____|_____
     |     |
  {self.spot[3]}  |  {self.spot[4]}  |  {self.spot[5]}
_____|_____|_____
     |     |
  {self.spot[6]}  |  {self.spot[7]}  |  {self.spot[8]}
     |     |

   """
        print(board)
    def get_input(self,player_name):
        
        while True:
            x = int(input(f"{player_name} enter your spot: "))
            x-= 1
            if 0 <= x < 9 :
                if x in self.index_list:
                    print("This spot is already taken")
                
                else:
                    self.index_list.append(x)
                    return(x)
                    break
            else:
                print("please enter number between 1-9")

    

    def game_winner(self,player_1,player_2):
        
        
        if (self.spot[0] == self.spot[1] == self.spot[2] == 'X' or self.spot[3] == self.spot[4] == self.spot[5] == 'X'or

        self.spot[6] == self.spot[7] == self.spot[8] == 'X' or self.spot[0] == self.spot[3] == self.spot[6] == 'X' or

        self.spot[1] == self.spot[4] == self.spot[7] == 'X' or self.spot[2] == self.spot[5] == self.spot[8] == 'X' or
       
        self.spot[0] == self.spot[4] == self.spot[8] == 'X' or self.spot[2] == self.spot[4] == self.spot[6] == 'X'):

            self.winner+= 1
            self.spot=[]
            self.index_list=[]
            print("Congratulations!",player_1,"you won the game! \nbetter luck next time",player_2)

           
        elif (self.spot[0] == self.spot[1] == self.spot[2] == 'O' or self.spot[3] == self.spot[4] == self.spot[5] == 'O' or

       self.spot[6] == self.spot[7] == self.spot[8] == 'O' or self.spot[0] == self.spot[3] == self.spot[6] == 'O' or

       self.spot[1] == self.spot[4] == self.spot[7] == 'O' or self.spot[2] == self.spot[5] == self.spot[8] == 'O' or
       
       self.spot[0] == self.spot[4] == self.spot[8] == 'O' or self.spot[2] == self.spot[4] == self.spot[6] == 'O'):

            self.winner+=1
            self.spot=[]
            print("Congratulations",player_2,"you won the game \nbetter luck next time",player_1)
    
class main(game):
    def main_fuction(self):
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
        print("Welcome to TIC TAC TOE game!")
        player_1 = input("player number one enter your name : ")
        player_2 = input("player number two enter your name : ")
        print("Thank you for joining\n"+player_1+"'s sign will be : X\n"+player_2+"'s sign will be : O") 

        print(tic_tac_toe)
        input("press any key to start the game:")
        self.display_board()
        self.winner = 0

        count = 0
        for i in range(9):
            if self.winner == 0 :
                if i%2 == 0:
                    index = self.get_input(player_1)
                    self.spot[index] = 'X'
                else:
                    index = self.get_input(player_2)
                    self.spot[index] = 'O'
                self.display_board()
                self.game_winner(player_1,player_2)
                count+=1
        if count == 9:
            print("the game is a tie")
        self.attempt+=1
        print(self.attempt)
main_obj = main()
main_obj.main_fuction()

play_again = input("do you wanna play the game again yes/no:").lower()


if play_again == "yes":
    main_obj.main_fuction()
else:
    print("Thank you for joining",player_1,"and",player_2)
