import pygame as pg
from random import randint

class Bil:
    def __init__(self, hjul, motortype):
        self.hjul = hjul
        self.motortype = motortype

    def kjor(self):
        print("Broombroom")

bil = Bil(4, "V8")
bil.kjor()

SCREEN_W = 800
SCREEN_H = 600

def tilfeldig_farge():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Spiller:
    def __init__(self, x, y, width, height, taster, color=None):
        if color == None:
            self.color = tilfeldig_farge()
        else:
            self.color = color
        self.keys = taster
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def update(self):
        keys = pg.key.get_pressed()

        if keys[self.keys["left"]]:
            self.rect.x -= 10

        if keys[self.keys["right"]]:
            self.rect.x += 10

        if keys[self.keys["up"]]:
            self.rect.y -= 10

        if keys[self.keys["down"]]:
            self.rect.y += 10


spiller1_taster = {"left": pg.K_LEFT, "right": pg.K_RIGHT, "up": pg.K_UP, "down": pg.K_DOWN}
spiller2_taster = {"left": pg.K_a, "right": pg.K_d, "up": pg.K_w, "down": pg.K_s}

spiller1 = Spiller(0, 0, 100, 100, spiller1_taster)
spiller2 = Spiller(100, 100, 50, 50, spiller2_taster)
spillere = [spiller1, spiller2]

dictionary = dict()

dictionary["hallo"] = 20
dictionary[20] = "hei"
dictionary["hei"] = "hallo"



print(dictionary)



pg.init()
screen = pg.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)

x = 0
y = 0

while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.KEYDOWN:

            for spiller in spillere:
                spiller.update()

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                pg.quit()
                quit()


    screen.fill((0, 0, 0))

    for spiller in spillere:
        spiller.draw(screen)

    pg.display.update()