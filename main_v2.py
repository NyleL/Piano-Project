from game import Game
from tkinter import *
from PIANO_PROJECT import *


# notes = [48, 49, 50]
# count = 0
# Piano_Dict = {48: my_gui.C_0_button, 49: my_gui.CC_0_button, 50: my_gui.D_0_button, 51: my_gui.DD_0_button, 52: my_gui.E_0_button, 53: my_gui.F_0_button, 54: my_gui.FF_0_button, 55: my_gui.G_0_button, 56: my_gui.GG_0_button, 57: my_gui.A_0_button, 58: my_gui.AA_0_button, 59: my_gui.B_0_button, 60: my_gui.C_1_button, 61: my_gui.CC_1_button,
# 				62: my_gui.D_1_button, 63: my_gui.DD_1_button,
# 				64: my_gui.E_1_button, 65: my_gui.F_1_button,
# 				66: my_gui.FF_1_button, 67: my_gui.G_1_button,
# 				68: my_gui.GG_1_button, 69: my_gui.A_1_button,
# 				70: my_gui.AA_1_button, 71: my_gui.B_1_button,}

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
