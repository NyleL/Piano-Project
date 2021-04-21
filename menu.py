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
        self.majox, self.majoy = self.mid_w, self.mid_h + 20
        self.minox, self.minoy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majox + self.offset, self.majoy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("C Major", 15, self.majox, self.majoy)

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
                self.game.curr_menu = self.game.piano_gui
            self.run_display = False

class Piano_gui(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)

    def display_menu(self):
        self.run_display = True
        pianomain()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("C Major", 15, self.majx, self.majy)

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
                self.game.curr_menu = self.game.piano_gui
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








