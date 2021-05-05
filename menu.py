import pygame
from PIANO_PROJECT import *
#from main_v2 import *



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Quiz Me", 20, self.startx, self.starty)
            self.game.draw_text("Study Music", 20, self.optionsx, self.optionsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Chords'
        self.chordsx, self.chordsy = self.mid_w, self.mid_h + 20
        self.scalesx, self.scalesy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.chordsx + self.offset, self.chordsy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Chords", 15, self.chordsx, self.chordsy)
            self.game.draw_text("Scales", 15, self.scalesx, self.scalesy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Chords':
                self.state = 'Scales'
                self.cursor_rect.midtop = (self.scalesx + self.offset, self.scalesy)
            elif self.state == 'Scales':
                self.state = 'Chords'
                self.cursor_rect.midtop = (self.chordsx + self.offset, self.chordsy)
        elif self.game.START_KEY:
            if self.state == 'Chords':
                self.game.curr_menu = self.game.major_minor
            elif self.state =='Scales':
                self.game.curr_menu = self.game.major_minor
            self.run_display = False


class Major_Minor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Major'
        self.majorx, self.majory = self.mid_w, self.mid_h + 20
        self.minorx, self.minory = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majorx + self.offset, self.majory)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Major", 15, self.majorx, self.majory)
            self.game.draw_text("Minor", 15, self.minorx, self.minory)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Major':
                self.state = 'Minor'
                self.cursor_rect.midtop = (self.minorx + self.offset, self.minory)
            elif self.state == 'Minor':
                self.state = 'Major'
                self.cursor_rect.midtop = (self.majorx + self.offset, self.majory)
        elif self.game.START_KEY:
            if self.state == "Major":
                self.game.curr_menu = self.game.majorlist
            self.run_display = False
            # CREATE NEW MAJOR MINOR LIST



class Major_Chords(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Majo'
        self.majox, self.majoy = self.mid_w, self.mid_h + -60
        self.minoa, self.minob = self.mid_w, self.mid_h + -40
        self.minoc, self.minod = self.mid_w, self.mid_h + -20
        self.minoe, self.minof = self.mid_w, self.mid_h + 0
        self.minog, self.minoh = self.mid_w, self.mid_h + 20
        self.minoi, self.minoj = self.mid_w, self.mid_h + 40
        self.minok, self.minol = self.mid_w, self.mid_h + 60

        self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H /5)
            self.game.draw_text("C Major", 15, self.majox, self.majoy)
            self.game.draw_text("D Major", 15, self.minoa, self.minob)
            self.game.draw_text("E Major", 15, self.minoc, self.minod)
            self.game.draw_text("F Major", 15, self.minoe, self.minof)
            self.game.draw_text("G Major", 15, self.minog, self.minoh)
            self.game.draw_text("A Major", 15, self.minoi, self.minoj)
            self.game.draw_text("B Major", 15, self.minok, self.minol)


            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Majo':
                self.state = 'minoa'
                self.cursor_rect.midtop = (self.minoa + self.offset, self.minob)
            elif self.state == 'minoa':
                self.state = 'minoc'
                self.cursor_rect.midtop = (self.minoc + self.offset, self.minod)
            elif self.state == 'minoc':
                self.state = 'minoe'
                self.cursor_rect.midtop = (self.minoe + self.offset, self.minof)
            elif self.state == 'minoe':
                self.state = 'minog'
                self.cursor_rect.midtop = (self.minog + self.offset, self.minoh)
            elif self.state == 'minog':
                self.state = 'minoi'
                self.cursor_rect.midtop = (self.minoi + self.offset, self.minoj)
            elif self.state == 'minoi':
                self.state = 'minok'
                self.cursor_rect.midtop = (self.minok + self.offset, self.minol)
            elif self.state == 'minok':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.UP_KEY:
            if self.state == 'Majo':
                self.state = 'minok'
                self.cursor_rect.midtop = (self.minok + self.offset, self.minol)
            elif self.state == 'minok':
                self.state = 'minoi'
                self.cursor_rect.midtop = (self.minoi + self.offset, self.minoj)
            elif self.state == 'minoi':
                self.state = 'minog'
                self.cursor_rect.midtop = (self.minog + self.offset, self.minoh)
            elif self.state == 'minog':
                self.state = 'minoe'
                self.cursor_rect.midtop = (self.minoe + self.offset, self.minof)
            elif self.state == 'minoe':
                self.state = 'minoc'
                self.cursor_rect.midtop = (self.minoc + self.offset, self.minod)
            elif self.state == 'minoc':
                self.state = 'minoa'
                self.cursor_rect.midtop = (self.minoa + self.offset, self.minob)
            elif self.state == 'minoa':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.START_KEY:
            if self.state == "Majo":
                self.game.curr_menu = self.game.piano_gui
            if self.state == "minoa":
                self.game.curr_menu = self.game.DMajor
            if self.state == "minoc":
                self.game.curr_menu = self.game.EMajor
            if self.state == "minoe":
                self.game.curr_menu = self.game.FMajor
            self.run_display = False

class Piano_gui(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        c_major =[48, 52, 55]
        pianomain(self.game.root, self.game.my_gui, c_major)
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Gui", 15, self.majx, self.majy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Majo':
                self.state = 'Mino'
                self.cursor_rect.midtop = (self.minox + self.offset, self.minoy)
            elif self.state == 'Mino':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.START_KEY:
            if self.state == "Majo":
                self.game.curr_menu = self.game.DMajor
            self.run_display = False

class DMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        d_major =[50, 53, 56]
        pianomain(self.game.root, self.game.my_gui, d_major)
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Gui", 15, self.majx, self.majy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Majo':
                self.state = 'Mino'
                self.cursor_rect.midtop = (self.minox + self.offset, self.minoy)
            elif self.state == 'Mino':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.START_KEY:
            if self.state == "Majo":
                self.game.curr_menu = self.game.DMajor
            self.run_display = False

class EMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        E_major =[54, 56, 58]
        pianomain(self.game.root, self.game.my_gui, E_major)
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Gui", 15, self.majx, self.majy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Majo':
                self.state = 'Mino'
                self.cursor_rect.midtop = (self.minox + self.offset, self.minoy)
            elif self.state == 'Mino':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.START_KEY:
            if self.state == "Majo":
                self.game.curr_menu = self.game.DMajor
            self.run_display = False

class FMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        F_major =[54, 56, 58]
        pianomain(self.game.root, self.game.my_gui, F_major)
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Gui", 15, self.majx, self.majy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Majo':
                self.state = 'Mino'
                self.cursor_rect.midtop = (self.minox + self.offset, self.minoy)
            elif self.state == 'Mino':
                self.state = 'Majo'
                self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)
        elif self.game.START_KEY:
            if self.state == "Majo":
                self.game.curr_menu = self.game.DMajor
            self.run_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()








