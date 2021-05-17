import pygame
from PIANO_PROJECT import *


# from main_v2 import *


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
                self.game.curr_menu = self.game.quizme
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class Quizme(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        song = [48, 52, 55]
        key_correct_percent = pianomain(self.game.root, self.game.my_gui, song,)
        print(key_correct_percent)
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text("Percent Correct: "+ str(key_correct_percent * 100) + "%",15, self.minx, self.miny)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
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
            elif self.state == 'Scales':
                self.game.curr_menu = self.game.scalelist
            self.run_display = False


class Scale_List(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Minora'
        self.minorax, self.minorby = self.mid_w, self.mid_h + -60
        self.minorcx, self.minordy = self.mid_w, self.mid_h + -40
        self.minorex, self.minorfy = self.mid_w, self.mid_h + -20
        self.minorgx, self.minorhy = self.mid_w, self.mid_h + 0
        self.minorix, self.minorjy = self.mid_w, self.mid_h + 20
        self.minorkx, self.minorly = self.mid_w, self.mid_h + 40
        self.minormx, self.minorny = self.mid_w, self.mid_h + 60

        self.cursor_rect.midtop = (self.minorax + self.offset, self.minorby)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 5)
            self.game.draw_text("C Scale", 15, self.minorax, self.minorby)
            self.game.draw_text("D Scale", 15, self.minorcx, self.minordy)
            self.game.draw_text("E Scale", 15, self.minorex, self.minorfy)
            self.game.draw_text("F Scale", 15, self.minorgx, self.minorhy)
            self.game.draw_text("G Scale", 15, self.minorix, self.minorjy)
            self.game.draw_text("A Scale", 15, self.minorkx, self.minorly)
            self.game.draw_text("B Scale", 15, self.minormx, self.minorny)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY:
            if self.state == 'Minora':
                self.state = 'Minorm'
                self.cursor_rect.midtop = (self.minormx + self.offset, self.minorny)
            elif self.state == 'Minorm':
                self.state = 'Minork'
                self.cursor_rect.midtop = (self.minorkx + self.offset, self.minorly)
            elif self.state == 'Minork':
                self.state = 'Minori'
                self.cursor_rect.midtop = (self.minorix + self.offset, self.minorjy)
            elif self.state == 'Minori':
                self.state = 'Minorg'
                self.cursor_rect.midtop = (self.minorgx + self.offset, self.minorhy)
            elif self.state == 'Minorg':
                self.state = 'Minore'
                self.cursor_rect.midtop = (self.minorex + self.offset, self.minorfy)
            elif self.state == 'Minore':
                self.state = 'Minorc'
                self.cursor_rect.midtop = (self.minorcx + self.offset, self.minordy)
            elif self.state == 'Minorc':
                self.state = 'Minora'
                self.cursor_rect.midtop = (self.minorax + self.offset, self.minorby)
        elif self.game.DOWN_KEY:
            if self.state == 'Minora':
                self.state = 'Minorc'
                self.cursor_rect.midtop = (self.minorcx + self.offset, self.minordy)
            elif self.state == 'Minorc':
                self.state = 'Minore'
                self.cursor_rect.midtop = (self.minorex + self.offset, self.minorfy)
            elif self.state == 'Minore':
                self.state = 'Minorg'
                self.cursor_rect.midtop = (self.minorgx + self.offset, self.minorhy)
            elif self.state == 'Minorg':
                self.state = 'Minori'
                self.cursor_rect.midtop = (self.minorix + self.offset, self.minorjy)
            elif self.state == 'Minori':
                self.state = 'Minork'
                self.cursor_rect.midtop = (self.minorkx + self.offset, self.minorly)
            elif self.state == 'Minork':
                self.state = 'Minorm'
                self.cursor_rect.midtop = (self.minormx + self.offset, self.minorny)
            elif self.state == 'Minorm':
                self.state = 'Minora'
                self.cursor_rect.midtop = (self.minorax + self.offset, self.minorby)
        elif self.game.START_KEY:
            if self.state == "Minora":
                self.game.curr_menu = self.game.CScale
            if self.state == "Minorc":
                self.game.curr_menu = self.game.DScale
            if self.state == "Minore":
                self.game.curr_menu = self.game.EScale
            if self.state == "Minorg":
                self.game.curr_menu = self.game.FScale
            if self.state == "Minori":
                self.game.curr_menu = self.game.GScale
            if self.state == "Minork":
                self.game.curr_menu = self.game.AScale
            if self.state == "Minorm":
                self.game.curr_menu = self.game.BScale
            self.run_display = False

            self.draw_cursor()
            self.blit_screen()


class CScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        c_scale = [48, 50, 52, 53, 55, 57, 59, 60]
        pianomain(self.game.root, self.game.my_gui, c_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.DScale
            self.run_display = False


class DScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        d_scale = [50, 52, 53, 55, 57, 59, 60, 62]
        pianomain(self.game.root, self.game.my_gui, d_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.EScale
            self.run_display = False


class EScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        e_scale = [52, 53, 55, 57, 59, 60, 62, 64]
        pianomain(self.game.root, self.game.my_gui, e_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.FScale
            self.run_display = False


class FScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        f_scale = [53, 55, 57, 59, 60, 62, 64, 65]
        pianomain(self.game.root, self.game.my_gui, f_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.GScale
            self.run_display = False


class GScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        g_scale = [55, 57, 59, 60, 62, 64, 65, 67]
        pianomain(self.game.root, self.game.my_gui, g_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.AScale
            self.run_display = False


class AScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        a_scale = [57, 59, 60, 62, 64, 65, 67, 69]
        pianomain(self.game.root, self.game.my_gui, a_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.BScale
            self.run_display = False


class BScale(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        b_scale = [59, 60, 62, 64, 65, 67, 69, 71]
        pianomain(self.game.root, self.game.my_gui, b_scale)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.CScale
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
            elif self.state == "Minor":
                self.game.curr_menu = self.game.minorlist
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
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 5)
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
            self.game.curr_menu = self.game.major_minor
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
            if self.state == "minog":
                self.game.curr_menu = self.game.GMajor
            if self.state == "minoi":
                self.game.curr_menu = self.game.AMajor
            if self.state == "minok":
                self.game.curr_menu = self.game.BMajor

            self.run_display = False


class Minor_Chords(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + -60
        self.mina, self.minb = self.mid_w, self.mid_h + -40
        self.minc, self.mind = self.mid_w, self.mid_h + -20
        self.mine, self.minf = self.mid_w, self.mid_h + 0
        self.ming, self.minh = self.mid_w, self.mid_h + 20
        self.mini, self.minj = self.mid_w, self.mid_h + 40
        self.mink, self.minl = self.mid_w, self.mid_h + 60

        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Choose Mode ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 5)
            self.game.draw_text("C Minor", 15, self.majx, self.majy)
            self.game.draw_text("D Minor", 15, self.mina, self.minb)
            self.game.draw_text("E Minor", 15, self.minc, self.mind)
            self.game.draw_text("F Minor", 15, self.mine, self.minf)
            self.game.draw_text("G Minor", 15, self.ming, self.minh)
            self.game.draw_text("A Minor", 15, self.mini, self.minj)
            self.game.draw_text("B Minor", 15, self.mink, self.minl)

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.major_minor
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Maj':
                self.state = 'mina'
                self.cursor_rect.midtop = (self.mina + self.offset, self.minb)
            elif self.state == 'mina':
                self.state = 'minc'
                self.cursor_rect.midtop = (self.minc + self.offset, self.mind)
            elif self.state == 'minc':
                self.state = 'mine'
                self.cursor_rect.midtop = (self.mine + self.offset, self.minf)
            elif self.state == 'mine':
                self.state = 'ming'
                self.cursor_rect.midtop = (self.ming + self.offset, self.minh)
            elif self.state == 'ming':
                self.state = 'mini'
                self.cursor_rect.midtop = (self.mini + self.offset, self.minj)
            elif self.state == 'mini':
                self.state = 'mink'
                self.cursor_rect.midtop = (self.mink + self.offset, self.minl)
            elif self.state == 'mink':
                self.state = 'Maj'
                self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        elif self.game.UP_KEY:
            if self.state == 'Maj':
                self.state = 'mink'
                self.cursor_rect.midtop = (self.mink + self.offset, self.minl)
            elif self.state == 'mink':
                self.state = 'mini'
                self.cursor_rect.midtop = (self.mini + self.offset, self.minj)
            elif self.state == 'mini':
                self.state = 'ming'
                self.cursor_rect.midtop = (self.ming + self.offset, self.minh)
            elif self.state == 'ming':
                self.state = 'mine'
                self.cursor_rect.midtop = (self.mine + self.offset, self.minf)
            elif self.state == 'mine':
                self.state = 'minc'
                self.cursor_rect.midtop = (self.minc + self.offset, self.mind)
            elif self.state == 'minc':
                self.state = 'mina'
                self.cursor_rect.midtop = (self.mina + self.offset, self.minb)
            elif self.state == 'mina':
                self.state = 'Maj'
                self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        elif self.game.START_KEY:
            if self.state == "Maj":
                self.game.curr_menu = self.game.CMinor
            if self.state == "mina":
                self.game.curr_menu = self.game.DMinor
            if self.state == "minc":
                self.game.curr_menu = self.game.EMinor
            if self.state == "mine":
                self.game.curr_menu = self.game.FMinor
            if self.state == "ming":
                self.game.curr_menu = self.game.GMinor
            if self.state == "mini":
                self.game.curr_menu = self.game.AMinor
            if self.state == "mink":
                self.game.curr_menu = self.game.BMinor

            self.run_display = False


class CMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        c_minor = [48, 51, 55]
        pianomain(self.game.root, self.game.my_gui, c_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.DMinor
            self.run_display = False


class DMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        d_minor = [50, 53, 57]
        pianomain(self.game.root, self.game.my_gui, d_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.EMinor
            self.run_display = False


class EMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        E_minor = [52, 55, 59]
        pianomain(self.game.root, self.game.my_gui, E_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.FMinor
            self.run_display = False


class FMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        F_minor = [53, 56, 60]
        pianomain(self.game.root, self.game.my_gui, F_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.GMinor
            self.run_display = False


class GMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        G_minor = [55, 58, 61]
        pianomain(self.game.root, self.game.my_gui, G_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.AMinor
            self.run_display = False


class AMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        A_minor = [57, 60, 64]
        pianomain(self.game.root, self.game.my_gui, A_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.BMinor
            self.run_display = False


class BMinor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        B_minor = [59, 62, 66]
        pianomain(self.game.root, self.game.my_gui, B_minor)
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
            self.game.curr_menu = self.game.minorlist
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
                self.game.curr_menu = self.game.CMinor
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
        c_major = [48, 52, 55]
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
            self.game.curr_menu = self.game.majorlist
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
        d_major = [50, 54, 57]
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.EMajor
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
        E_major = [52, 56, 59]
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.FMajor
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
        F_major = [53, 57, 60]
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.GMajor
            self.run_display = False


class GMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        G_major = [55, 59, 62]
        pianomain(self.game.root, self.game.my_gui, G_major)
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.AMajor
            self.run_display = False


class AMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        A_major = [57, 61, 64]
        pianomain(self.game.root, self.game.my_gui, A_major)
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.BMajor
            self.run_display = False


class BMajor(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Maj'
        self.majx, self.majy = self.mid_w, self.mid_h + 20
        self.minx, self.miny = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.majx + self.offset, self.majy)
        self.game = game

    def display_menu(self):
        self.run_display = True
        B_major = [59, 63, 66]
        pianomain(self.game.root, self.game.my_gui, B_major)
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
            self.game.curr_menu = self.game.majorlist
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
                self.game.curr_menu = self.game.CMajor
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
