import pygame
import sys
import time
from sg_lib import file_works as fw


class Button:
    def __init__(self, loc, size, SCREEN, text=None):
        self.loc = [*loc]
        self.size = [*size]
        self.SCREEN = SCREEN
        self.sit = 0  # situation,durum
        self.style = {"bg": (73, 72, 72),
                      "ol": (143, 140, 140),
                      "fg": (210, 210, 210),
                      "blk": (0, 0, 0)}
        self.text = text
        self.pos = "overlap"

    def draw_b(self):
        if self.pos == "free":
            pygame.draw.rect(self.SCREEN, self.style["bg"], [self.loc, self.size], 3)
        elif self.pos == "overlap":
            pygame.draw.rect(self.SCREEN, self.style["ol"], [self.loc, self.size])
            pygame.draw.rect(self.SCREEN, self.style["bg"], [self.loc, self.size], 3)
        elif self.pos == "clicked":
            pygame.draw.rect(self.SCREEN, self.style["bg"], [self.loc, self.size])
            pygame.draw.rect(self.SCREEN, self.style["blk"], [self.loc, self.size], 2)
        self.draw_text()

    def is_overlap(self):
        mouse_loc = pygame.mouse.get_pos()
        if self.loc[0] <= mouse_loc[0] <= self.size[0] + self.loc[0]:
            if self.loc[1] <= mouse_loc[1] <= self.size[1] + self.loc[1]:
                self.pos = "overlap"
            else:
                self.pos = "free"
        else:
            self.pos = "free"

    def is_clicked(self, say):
        mouse_loc = pygame.mouse.get_pos()
        print(mouse_loc)
        if self.loc[0] <= mouse_loc[0] <= self.size[0] + self.loc[0]:
            if self.loc[1] <= mouse_loc[1] <= self.size[1] + self.loc[1]:
                self.pos = "clicked"
                if say == 0:
                    pygame.quit()
                    sys.exit()
                elif say == 1:
                    print("küçült")
                    return 1
                elif say == 2:
                    print("settings")
                    return 2
                elif say == 3:
                    print("add")
                    return 3
                    # tr = "sen"
                    # eng = "you"
                    # fw.add_word(tr,eng)
                elif say == 4:
                    print("ask")
                    return 4
                    # fw.ask_q()

    def draw_text(self):
        if self.text is not None:
            pygame.font.init()
            font = pygame.font.Font(pygame.font.get_default_font(), 20)
            text_surface = font.render(str(self.text), False, self.style["blk"])
            self.SCREEN.blit(text_surface, (self.loc[0] + 10, self.loc[1] + self.size[1] / 3))

    def take_text(self, text=None):
        if text is not None:
            self.text = text
            self.draw_text()
