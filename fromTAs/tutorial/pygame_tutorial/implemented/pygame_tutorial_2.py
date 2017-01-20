import pygame
import math

type = "1b"

class Canvas(object):
  # A drawing canvas
  def __init__(self):
    # Set up pygame window
    pygame.init()
    pygame.display.set_mode((400,300))
    pygame.display.set_caption("Pygame Demo")
    self.screen = pygame.display.get_surface()
    self.pos_x = 50
    self.pos_y = 50
    self.counter = 0
    
  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
	exit()
  
  def update(self):
    # Change position of objects
    self.pos_x = int(math.sin(math.radians(self.counter))*100) + 200
    self.pos_y = int(math.cos(math.radians(self.counter))*100) + 150
    self.counter += 0.1
    
  def draw_scene(self):
    # Draw a circle in the window
    self.screen.fill(pygame.Color("white"))
    pygame.draw.circle(self.screen, pygame.Color("green"), (self.pos_x,self.pos_y), 10, 6)
    pygame.display.flip()
    
  def run(self):
    # The main loop
    while 1:
      self.handle_events()
      self.update()
      self.draw_scene()
      
if __name__ == "__main__":
  cv = Canvas()
  cv.run()