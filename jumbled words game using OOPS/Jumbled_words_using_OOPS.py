import pandas as pd
import random as rd
data = pd.read_csv("jumbled_words.csv")
data.shape
data
start_game=f"""WELCOME TO JUMBLED WORDS GAME
There are three levels in this game
1.Easy
2.medium
3.hard
"""

class jumble_game:
    
    score=0
    def jumble(self,word):
        
         #here we are converting the word into list of characters
        word_list = list(word)
        
        while True:
        #shuffling the character using a random method shuffle
            rd.shuffle(word_list)
            jumbled_word = ""

        #converting shuffled list into string
    
            for i in word_list:
                jumbled_word  = jumbled_word + i
            if jumbled_word != word:
                print(jumbled_word.lower())
                break

    def game_score(self,i):
        #calculating the score
        self.answer = input("enter your answer:") 
        if self.answer.lower() == i.lower():
            self.score = self.score + 1
                
    def display(self):
        
        display="""*There are 10 words in this level
*Each word contains a score
*After completing all the words you will get your score*
        """
        print(display)
        input("press any key to start the game")
        print("here are your words to solve")

class level(jumble_game):
    
    def level_method(self):
        while True:
            while True:
                user_choice = input("Enter your choice:")
                try:
                    user_choice = int(user_choice)
                    break
                except ValueError:
                    print("Invalid input please enter a number")
                    
            if user_choice <=3:
                break
            else:
                print("Please enter a number between 1-3")
                
        self.display()
        level_mapper = { 1 : data.Easy ,2 : data.Medium ,3 : data.Hard }
        level = level_mapper.get(user_choice)
        level_list = []
            
    
        while True:
            i = rd.choice(level)
            if i not in level_list:
                level_list.append(i)
            if len(level_list) == 10:
                break
        for i in level_list:
            self.jumble(i)
            self.game_score(i)
        print("YOUR SCORE:",self.score)
        

level_obj = level()
print(start_game)
level_obj.level_method()        
        
    
