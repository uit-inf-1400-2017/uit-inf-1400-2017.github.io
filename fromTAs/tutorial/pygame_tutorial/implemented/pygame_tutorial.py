import pygame

type = "1b"

class Canvas(object):
  # A drawing canvas
  def __init__(self):
    # Set up pygame window
    pygame.init()
    pygame.display.set_mode((400,300))
    pygame.display.set_caption("Pygame Demo")
    self.screen = pygame.display.get_surface()
    
  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
	exit()
  
  def update(self):
    # Change position of objects
    pass
    
  def draw_scene(self):
    # Draw a circle in the window
    self.screen.fill(pygame.Color("white"))
    if type == "1a":
      pygame.draw.circle(self.screen, pygame.Color("green"), (100,100), 100, 6)
      pygame.draw.circle(self.screen, pygame.Color("blue"), (200,60), 40, 1)
      pygame.draw.circle(self.screen, pygame.Color("red"), (200,200), 70, 0)
    elif type == "1b":
      pygame.draw.circle(self.screen, pygame.Color("blue"), (50,50), 30, 4)
      pygame.draw.circle(self.screen, pygame.Color("black"), (120,50), 30, 4)
      pygame.draw.circle(self.screen, pygame.Color("red"), (190,50), 30, 4)
      pygame.draw.circle(self.screen, pygame.Color("yellow"), (85,85), 30, 4)
      pygame.draw.circle(self.screen, pygame.Color("green"), (155,85), 30, 4)
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