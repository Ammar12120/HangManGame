#!/usr/bin/env python

import random
from time import sleep  

class HMPlayer:
    """This is a generic player for the hangman game"""
    def __init__(self, name:str) ->  None:
        """Constructor, needs the player's name"""
        self.name = name
        self.lives = 5

    def propose_letter(self):
        print("WARNING! To be reimplemented in the derived class!")
        raise NotImplementedError

    def __str__(self) -> str:
        return "{} has {} lives left.".format(self.name, self.lives)
    
    def __lt__(self,other):
        return self.lives < other.lives 
    

class HMHumanPlayer(HMPlayer):
    """A class to represent HangMan human player."""
    def __init__(self, name:str) -> None:
        super().__init__(name)

    def propose_letter(self) -> str:
        sleep(1)
        letter = ""
        while len(letter) != 1:
            letter = input("Propose a letter: ")
        return letter
    
    
class HMAIPlayer(HMPlayer):
    """A class to represent HangMan AI player."""
    def __init__(self, name:str) -> None:
        super().__init__(name+"_bot")
        self.propose_letters = []

    def propose_letter(self) -> str:
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        while letter in self.propose_letters:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.propose_letters.append(letter)
        return letter

    