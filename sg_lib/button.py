import pygame,sys

class Button():
    def __init__(self,loc,size,SCREEN,text = None):
        self.loc = [*loc]
        self.size = [*size]
        self.SCREEN = SCREEN

        self.style = {"bg" : (73, 72, 72),
                      "ol" : (143, 140, 140),
                      "fg" : (210, 210, 210),
                      "blk": (0,0,0)}
        self.text = text
        self.pos = "overlap"


    def draw_b(self):
        if self.pos == "free":
            pygame.draw.rect(self.SCREEN,self.style["bg"],[(self.loc),(self.size)],3)
        elif self.pos == "overlap":
            pygame.draw.rect(self.SCREEN,self.style["bg"],[(self.loc),(self.size)],3)
            pygame.draw.rect(self.SCREEN,self.style["ol"],[(self.loc),(self.size)])
        elif self.pos == "clicked":
            pygame.draw.rect(self.SCREEN,self.style["bg"],[(self.loc),(self.size)])
        self.draw_text()
        

    def is_overlap(self,say):
        mouse_loc = pygame.mouse.get_pos()
        print(mouse_loc)
        if mouse_loc[0] >= self.loc[0] and mouse_loc[0] <= self.size[0]+self.loc[0]:
            if mouse_loc[1] >= self.loc[1] and mouse_loc[1] <= self.size[1]+self.loc[1]:
                self.pos = "clicked"
                if say == 0:
                    pygame.quit()
                    sys.exit()
                elif say == 1:
                    print("küçült")
                elif say == 2:
                    print("settings")
                elif say == 3:
                    print("ask")
                elif say == 4:
                    print("add")

    def draw_text(self,):
        if self.text != None:
            pygame.font.init()
            font = pygame.font.Font(pygame.font.get_default_font(), 20)
            text_surface = font.render(str(self.text), False, self.style["blk"])
            self.SCREEN.blit(text_surface,(self.loc[0]+10,self.loc[1]+self.size[1]/3))
                

