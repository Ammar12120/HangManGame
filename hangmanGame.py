#!/usr/bin/env python

import random
from players import *

class HMGame:
    """"HangMan game manager class"""
    def __init__(self,players:list) -> None:
        self.word = None
        self.players = players
        self.guessed_letters = []

    def display_word(self) -> str:
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_ "
        return display

    def play(self):
        for p in self.players:
            self.word = random.choice(["dog", "cat", "house", "pencil", "music", "banana", "hospital"])
            self.guessed_letters = []
            while p.lives > 0 and self.word != self.display_word():
                print('---------------------------------------------------')
                self.turn(p)
            if self.word == self.display_word():
                print("Congratulations {}, you won!".format(p.name))
            else:   
                print("Player {} lost!".format(p.name))
        # TODO: Improve win condition. Check for draws and winner lives > 0.
        print("The player that has won the game is {}".format(max(self.players)))
                
    def turn(self, p:HMPlayer) -> None:
        print("Player {}. Word: {}".format(p.name, self.display_word()))
        l = p.propose_letter()
        print("Player {} propose letter: {}".format(p.name, l))
        if l in self.word and l not in self.guessed_letters: # TODO: Decide if repeating letter must substract a live
            print("Good guess!\n")
            self.guessed_letters.append(l)
        else:
            print("Worng guess\n")
            p.lives -= 1


        