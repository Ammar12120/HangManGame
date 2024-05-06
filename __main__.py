#!/usr/bin/env python3
from players import *
from hangmanGame import HMGame

import players

def main():
    p1 = HMHumanPlayer("aa")
    p2 = HMAIPlayer("bb")
    players = [p1, p2]
    game = HMGame(players)
    game.play()

if __name__=="__main__":
    main()
