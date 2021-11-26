from sg_lib import button as bf
from sg_lib import file_works as fw
from sg_lib import button_wrt as wrt
import random,sys,os, pygame,time

pygame.init()
disp_info = pygame.display.Info()
comp_sizes = (disp_info.current_w, disp_info.current_h)
WIDTH, HEIGHT = [int(comp_sizes[0]/5),int(comp_sizes[1]/5)]
x, y = (comp_sizes[0] - WIDTH - 30, comp_sizes[1] - HEIGHT - 45)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT], pygame.NOFRAME)

class Interface():
    def __init__(self):
        global comp_sizes,SCREEN
        self.WIDTH, self.HEIGHT = [int(comp_sizes[0]/5),int(comp_sizes[1]/5)]
        x, y = (comp_sizes[0] - self.WIDTH - 30, comp_sizes[1] - self.HEIGHT - 45)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
        self.SCREEN = SCREEN

        self.style = {"bg" : (73, 72, 72),
                      "fg" : (210, 210, 210),
                      "blk": (0,0,0)}

        self.display_strt()
        self.is_open = True
        self.is_open_ask = False
        self.main_loop()

    def display_strt(self):
        rect_range = [self.WIDTH,0]
        while rect_range[0] > 0:
            rect_range[0] -= 5
            time.sleep(0.007)
            self.back_clr = self.style["blk"]
            self.SCREEN.fill(self.back_clr)
            pygame.draw.rect(self.SCREEN,self.style["fg"],[rect_range,(self.WIDTH,self.HEIGHT)])
            pygame.display.flip()
        self.back_clr = self.style["fg"]

    def main_loop(self):
        global WIDTH, HEIGHT
        if self.is_open:
            button_list = [bf.Button((WIDTH-30,10),(20,20),self.SCREEN),
                           bf.Button((WIDTH-40,HEIGHT-40),(30,30),self.SCREEN),
                           bf.Button((WIDTH-40,HEIGHT-80),(30,30),self.SCREEN),
                           bf.Button((10,10),(150,50),self.SCREEN,"add word"),
                           bf.Button((10,HEIGHT-60),(150,50),self.SCREEN,"ask question")]
        elif self.is_open_ask:
            button_list = [bf.Button((WIDTH-30,10),(20,20),self.SCREEN),
                           bf.Button((WIDTH-40,HEIGHT-40),(30,30),self.SCREEN)]
        while self.is_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    say = 0
                    for button in button_list:
                        button.is_clicked(say)
                        say+=1
                else:
                    for button in button_list:
                        button.is_overlap()

            self.SCREEN.fill(self.back_clr)
            for button in button_list:
                button.draw_b()
            pygame.display.flip()

        while self.is_open_ask:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    say = 0
                    for button in button_list:
                        button.is_clicked(say)
                        say+=1
                

                
                    



mainloop = Interface()



