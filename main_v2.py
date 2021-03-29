from game import Game
from tkinter import *
from PIANO_PROJECT import *




g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
