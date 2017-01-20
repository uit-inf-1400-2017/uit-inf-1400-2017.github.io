# Marius Andreassen

# Standard libraries
import math
from random import randrange

# Third party libraries
import pygame

# Global constants
SCREEN_W           = 1024
SCREEN_H           = 768
ADD_INTERVAL       = 1000000
COLLISION_FRICTION = 0.8
BACKGROUND         = (0, 0, 0)
ANIMATION_SCALE    = 0.05 # eqv. 50 FPS
LOW_SPEED          = 0.5


class Vector2D():
    """ Implements a two dimensional vector. """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vector(X: {x}, Y: {y})'.format(x = self.x, y = self.y)
            
    def __add__(self, b):
        """ Addition. Returns a new vector. """
        return Vector2D(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        """ Subtraction. Returns a new vector. """
        return Vector2D(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        """ Multiplication by a scalar. Note that the scalar must be to the right. """            
        try:
            b = float(b)
            return Vector2D(self.x * b, self.y * b)
        except ValueError:
            print("Oops! Right value must be a float")
            raise

    def magnitude(self):
        """ Returns the magnitude of the vector. """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        """ Returns a new vector with the same direction but magnitude 1. """
        try:
            m = self.magnitude()
            return Vector2D(self.x / m, self.y / m)
        except ZeroDivisionError:
            print("Oops! Cannot normalize a zero-vector")
            raise

    def copy(self):
        """ Returns a copy of the vector. """
        return Vector2D(self.x, self.y)
       
      
class Ball():
    """ Ball class """
    def __init__(self, x, y):
        self.pos    = Vector2D(x, y)
        self.speed  = Vector2D(randrange(5, 30), randrange(-7, -2))
        self.radius = randrange(30, 70)
        self.color  = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        self.ttl    = 5000.0

    def wall_collision(self):
        """ Handle wall collision """        
        # Right wall
        if (self.pos.x + self.radius) >= SCREEN_W and self.speed.x > 0:            
            self.speed   *= COLLISION_FRICTION
            self.speed.x *= -1

        # Left wall
        if (self.pos.x - self.radius) <= 0 and self.speed.x < 0:
            self.speed   *= COLLISION_FRICTION
            self.speed.x *= -1

        # Roof
        if (self.pos.y - self.radius) <= 0 and self.speed.y < 0:
            self.speed   *= COLLISION_FRICTION
            self.speed.y *= -1

        # Floor
        if (self.pos.y + self.radius) >= SCREEN_H and self.speed.y > 0:
            self.speed   *= COLLISION_FRICTION
            self.speed.y *= -1

    def move(self, animation_step):
        """ Move ball based on speed and animation step """        
        if self.speed.magnitude() > LOW_SPEED:
            self.speed.y += (animation_step * ANIMATION_SCALE)            # Gravity
            self.pos += self.speed * (animation_step * ANIMATION_SCALE)   # Move
        else:
            self.ttl -= animation_step                                    # Decrease ball->life if speed is low 

    def draw(self, screen):
        """ Draw ball with pygame.draw.circle """        
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)


class BouncingBalls():
    """ Main bouncing balls class """
    def __init__(self):
        self.screen       = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.ballist      = []
        self.balladder    = 0
        self.keep_running = True

    def add_ball(self, animation_step):
        """ Add ball to list if given time interval has past """
        self.balladder += randrange(0, 1000) * animation_step
        if self.balladder > ADD_INTERVAL:
            self.balladder = 0
            self.ballist.append(Ball(0, randrange(50, 250)))

    def draw(self, animation_step):
        """ Run all balls in ballist """
        self.screen.fill(BACKGROUND)       # Fill screen with background color
        for ball in self.ballist:          # Run all balls in list
            ball.wall_collision()
            ball.move(animation_step)            
            ball.draw(self.screen)
            if ball.ttl <= 0:
                self.ballist.remove(ball)

        pygame.display.update()             # Update display 

    def event_handler(self):
        """ Handle input """
        for event in pygame.event.get():           # Poll events    
            if event.type == pygame.QUIT:               # If event is quit, 
                self.keep_running = False                   # break main loop
            if event.type == pygame.KEYDOWN:            # If ESC-button is pressd 
                if event.key == pygame.K_ESCAPE:            # break main loop
                    self.keep_running = False

    def run(self):    
        """ Run main loop for bouncing balls animation """   
        stime = 0
        etime = 0
        
        while self.keep_running:             
            stime = pygame.time.get_ticks()         # Get current time 
            
            self.event_handler()                    # Run event handler            
            self.add_ball(etime)                    # Add ball to list in given time interval
            self.draw(etime)                        # Run animation  

            etime = pygame.time.get_ticks() - stime # Calculate looptime

    
    
if __name__ == '__main__':
    
    pygame.init()

    new = BouncingBalls()

    new.run()
