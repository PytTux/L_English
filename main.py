from sg_lib import button as bf
from sg_lib import file_works as fw
from sg_lib import button_wrt as wrt
import os, pygame, time
from sys import exit

pygame.init()
disp_info = pygame.display.Info()
comp_sizes = (disp_info.current_w, disp_info.current_h)
WIDTH, HEIGHT = [int(comp_sizes[0] / 5), int(comp_sizes[1] / 5)]
x, y = (comp_sizes[0] - WIDTH - 30, comp_sizes[1] - HEIGHT - 45)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT], pygame.NOFRAME)


class Interface:
    def __init__(self):
        global comp_sizes, SCREEN
        self.WIDTH, self.HEIGHT = [int(comp_sizes[0] / 5), int(comp_sizes[1] / 5)]
        x_loc = comp_sizes[0] - self.WIDTH - 30
        y_loc = comp_sizes[1] - self.HEIGHT - 45
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_loc, y_loc)
        self.SCREEN = SCREEN

        self.style = {"bg": (73, 72, 72),
                      "fg": (210, 210, 210),
                      "blk": (0, 0, 0)}

        self.display_strt()
        self.is_open = True
        self.is_write = False
        self.text = ""

        self.main_loop()

    def display_strt(self):
        rect_range = [self.WIDTH, 0]
        self.back_clr = self.style["blk"]
        while rect_range[0] > 0:
            rect_range[0] -= 5
            time.sleep(0.007)
            self.SCREEN.fill(self.back_clr)
            pygame.draw.rect(self.SCREEN, self.style["fg"], [rect_range, (self.WIDTH, self.HEIGHT)])
            pygame.display.flip()
        self.back_clr = self.style["fg"]

    def main_loop(self):
        global WIDTH, HEIGHT
        back_count = 0
        if self.is_open:
            button_list = [bf.Button((WIDTH - 30, 10), (20, 20), self.SCREEN),
                           bf.Button((WIDTH - 40, HEIGHT - 40), (30, 30), self.SCREEN),
                           bf.Button((WIDTH - 40, HEIGHT - 80), (30, 30), self.SCREEN),
                           bf.Button((10, 10), (150, 50), self.SCREEN, "add word"),
                           bf.Button((10, HEIGHT - 60), (150, 50), self.SCREEN, "ask question")]
        while self.is_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.KEYDOWN and self.is_write:
                    print("ok")
                    print(event.key)
                    if event.key != 8:
                        back_count = 0
                    if event.key == 8:
                        if back_count >= 3:
                            self.text = ""
                        else:
                            self.text = self.text[:-1]
                            back_count += 1
                    elif event.key == 32:
                        self.text += " "
                    elif event.key == 13:
                        print("işlem bitti kaydedilicek e ya buttona gönderilcek")
                    elif event.key == 1073742049 or event.key == 1073741881 or event.key == 1073741907:
                        pass
                    else:
                        self.text = self.text + pygame.key.name(event.key)
                        print(self.text)
                    button_list[3].take_text(self.text)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    say = 0
                    self.is_write = False
                    for button in button_list:
                        button.is_clicked(say)
                        if button.is_clicked(say) == 3:  # add word
                            self.is_write = True
                            button_list[3].take_text("please write:")
                        # elif button.is_clicked(say) == 4:#ask_q

                        say += 1
                else:
                    for button in button_list:
                        button.is_overlap()

            self.SCREEN.fill(self.back_clr)
            for button in button_list:
                button.draw_b()
            pygame.display.flip()


mainloop = Interface()
