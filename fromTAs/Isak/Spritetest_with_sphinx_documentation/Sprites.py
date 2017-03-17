"""
Created on 17.03.2017
Isak Sunde Singh
Contains the code for the sprite testing stuff and things.
Professional comments only.
'Go here for more sphinx tips and tricks:
https://pythonhosted.org/an_example_pypi_project/sphinx.html
"""

import pygame
from Config import *


class Car(pygame.sprite.Sprite):
    """ Super basic car class with the best engine and color. 
        This car looks like:

        .. image:: ../beetle.png
           :align:  center

    """
    def __init__(self, engine=None, color="red", wheels=4):
        """ Constructor function for the class Car. This is a quite bad docstring. """
        super().__init__()
        self.engine = engine
        self.wheels = wheels
        self.color = color
        self.image = pygame.image.load("beetle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_W // 2, SCREEN_H // 2)

    def __repr__(self):
        representation = """
  ______
 /|_||_\`.__
(   _    _ _\\
=`-(_)--(_)-' """
        return representation



def get_col(color):
    """ Returns a color from the pygame THECOLORS color dictionary.

    :param color: The name of a color that lies in the pygame THECOLORS dictionary
    :type color: str
    :returns: tuple -- The color inputted as a tuple, the color blue will be returned if an invalid parameter was given.
    
    """
    return pygame.color.THECOLORS.get(color, pygame.color.THECOLORS["blue"])


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    beetle = Car()
    group = pygame.sprite.Group()
    group.add(beetle)
    print(beetle)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type is pygame.QUIT:
                running = not running   
        
        screen.fill(get_col("white"))
        group.draw(screen)
        pygame.display.update()

    pygame.quit()
    quit()