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
    self.left_pressed = False
    self.right_pressed = False
    self.up_pressed = False
    self.down_pressed = False
    
  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
	exit()
      elif event.type == pygame.KEYDOWN:
	if event.key == pygame.K_UP:
	  self.up_pressed = True
	elif event.key == pygame.K_DOWN:
	  self.down_pressed = True
	elif event.key == pygame.K_LEFT:
	  self.left_pressed = True
	elif event.key == pygame.K_RIGHT:
	  self.right_pressed = True
	elif event.key == pygame.K_ESCAPE:
	  exit()
      elif event.type == pygame.KEYUP:
	if event.key == pygame.K_UP:
	  self.up_pressed = False
	elif event.key == pygame.K_DOWN:
	  self.down_pressed = False
	elif event.key == pygame.K_LEFT:
	  self.left_pressed = False
	elif event.key == pygame.K_RIGHT:
	  self.right_pressed = False
  
  def update(self):
    # Change position of objects
    speed = 1
    if self.left_pressed == True:
      self.pos_x -= speed
    elif self.right_pressed == True:
      self.pos_x += speed
    elif self.up_pressed == True:
      self.pos_y -= speed
    elif self.down_pressed == True:
      self.pos_y += speed
      
    
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