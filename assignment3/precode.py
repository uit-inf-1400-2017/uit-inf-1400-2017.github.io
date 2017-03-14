#!/usr/bin/env python

""" Pre-code for INF-1400

16 January 2017 Revision 3 (Mads Johansen):
Rewritten to conform to Python 3 standard. Made class iterable, added property as_point,
replaced magnitude with __abs__ (to reflect mathematical vector notation), added rotate method.

22 January 2012 Revision 2 (Martin Ernstsen):
Reraise exception after showing error message.

11 February 2011 Revision 1 (Martin Ernstsen):
Fixed bug in intersect_circle. Updated docstrings to Python standard.
Improved __mul__. Added some exception handling. Put example code in separate
function.

"""

from math import hypot, cos, sin, radians
import pygame


class Vector2D(object):
    """Implements a two dimensional vector.

    :param x: First component for the vector.
    :param y: Second component for the vector.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({vec.x}, {vec.y})'.format(vec=self)

    def __str__(self):
        return 'Vector(X: {vec.x}, Y: {vec.y}) Magnitude: {lng}'.format(vec=self, lng=abs(self))

    def __nonzero__(self):
        """ Makes Vector2D(0,0) evaluate to False, all other vectors evaluate to True
        :returns: Boolean evaluation of vector. """
        return not self.as_point == (0, 0)

    __bool__ = __nonzero__

    def __add__(self, b):
        """ Vector addition.
        :returns: New vector where x = self.x + b.x and y = self.y + b.y
        """
        return Vector2D(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        """ Vector subtraction.
        :returns: New vector where x = self.x - b.x and y = self.y - b.y
        """
        return Vector2D(self.x - b.x, self.y - b.y)

    def __eq__(self, other):
        """ Vector equality.
        :returns: True of both components of this vector are equal to those of b.
        """
        return self.x == other.x and self.y == other.y

    def __mul__(self, b):
        """ Vector multiplication by a scalar.
        :param: Any value that can be coerced into a float.
        :returns: New vector where x = self.x * b and y = self.y * b
        """
        try:
            b = float(b)
            return Vector2D(self.x * b, self.y * b)
        except ValueError:
            raise ValueError("Right value must be a float, was {}".format(b))

    def __truediv__(self, b):
        """ Vector division by a scalar.
        :param: Any value that can be coerced into a float.
        :returns: New vector where x = self.x / b and y = self.y / b
        """
        try:
            b = float(b)
            return Vector2D(self.x / b, self.y / b)
        except ValueError:
            raise ValueError("Right value must be a float, was {}".format(b))

    def __iter__(self):
        """ Generator function used to iterate over components of vector.
        :returns: Iterator over components.
        """
        for value in self.__dict__.values():
            yield value

    def __rmul__(self, b):
        try:
            b = float(b)
            return Vector2D(self.x * b, self.y * b)
        except (ValueError, ZeroDivisionError):
            raise ValueError("Scalar must be a float, was {}".format(b))

    def __abs__(self):
        """ Returns the magnitude of the vector. """
        return hypot(self.x, self.y)

    def normalized(self):
        """ Returns a new vector with the same direction but magnitude 1.
        :returns: A new unit vector with the same direction as self.
        NOTE: Returns a unit vector of zero degrees if self has magnitude 0.
        """
        try:
            m = abs(self)
            return self / m
        except ZeroDivisionError:
            # Attempted to normalize a zero vector, return a unit vector at zero degrees
            return Vector2D(1, 0)

    def copy(self):
        """ Returns a copy of the vector.
        :returns: A new vector identical to self.
        """
        return Vector2D(self.x, self.y)

    @property
    def as_point(self):
        """ A tuple representation of the vector, useful for pygame functions.
        :returns: A tuple of the vectors components.
        """
        return round(self.x), round(self.y)

    def rotate(self, theta):
        """ Vector rotation.
        :param theta: The angle of rotation in degrees.
        :returns: A new vector which is the same length, but rotated by theta. """
        cos_theta, sin_theta = cos(radians(theta)), sin(radians(theta))
        newx = round(self.x * cos_theta - self.y * sin_theta, 6)
        newy = round(self.x * sin_theta + self.y * cos_theta, 6)
        return Vector2D(newx, newy)

def intersect_rectangle_circle(rec_pos, sx, sy, circle_pos, circle_radius, circle_speed):
    """ Determine if a rectangle and a circle intersects.
    
    Only works for a rectangle aligned with the axes.
    
    Parameters:
    rec_pos     - A Vector2D representing the position of the rectangles upper,
                  left corner.
    sx          - Width of rectangle.
    sy          - Height of rectangle.
    circle_pos  - A Vector2D representing the circle's position.
    circle_radius - The circle's radius.
    circle_speed - A Vector2D representing the circles speed.
    
    Returns:
    False if no intersection. If the rectangle and the circle intersect, returns
    a normalized Vector2D pointing in the direction the circle will move after
    the collision.
    
    """

    # Position of the walls relative to the ball
    top    = (rec_pos.y     ) - circle_pos.y
    bottom = (rec_pos.y + sy) - circle_pos.y 
    left   = (rec_pos.x     ) - circle_pos.x
    right  = (rec_pos.x + sx) - circle_pos.x

    r = circle_radius 
    intersecting = left <= r and top <= r and right >= -r and bottom >= -r

    if intersecting:
        # Now need to figure out the vector to return.
        # should be just a matter of flipping x and y of the ball?

        impulse = circle_speed.normalized()

        if abs(left) <= r and impulse.x > 0:
            impulse.x = -impulse.x
        if abs(right) <= r and impulse.x < 0:
            impulse.x = -impulse.x
        if abs(top) <= r and impulse.y > 0:
            impulse.y = -impulse.y
        if abs(bottom) <= r and impulse.y < 0:
            impulse.y = -impulse.y
            
        #print("Impact", circle_speed, impulse.normalized())

        return impulse.normalized()
    return False


def intersect_circles(a_pos, a_radius, b_pos, b_radius):
    """ Determine if two circles intersect.
    
    Parameters:
    a_pos       - A Vector2D representing circle A's position
    a_radius    - Circle A's radius
    b_pos       - A Vector2D representing circle B's position
    b_radius    - Circle B's radius
    
    Returns:
    False if no intersection. If the circles intersect, returns a normalized
    Vector2D pointing from circle A to circle B.
    
    """
    # vector from A to B 
    dp1p2 = b_pos - a_pos
    
    if a_radius + b_radius >= abs(dp1p2):
        return dp1p2.normalized()
    else:
        return False


def example_code():
    """ Example showing the use of the above code. """
    
    screen_res = (640,480)
    pygame.init()

    ra_pos = Vector2D(320, 320) # Rectangle A position
    ra_sx = ra_sy = 20 # Rectangle A size

    rb_pos = Vector2D(250, 250) # Rectangle B position
    rb_sx = rb_sy = 10 # Rectangle B stretch

    # Tracks the mouse cursor
    a_pos = Vector2D(10, 10) # Circle A position
    a_radius = 6 # Circle A radius
    a_speed = Vector2D(5,5) # Circle A speed

    b_pos = Vector2D(150, 150) # Circle B position
    b_radius = 10 # Circle B radius
    b_speed = Vector2D(5,5) # Circle B speed

    screen = pygame.display.set_mode(screen_res)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
        pygame.draw.rect(screen, (0,0,0), (0, 0, screen.get_width(), screen.get_height()))
        time_passed = clock.tick(30) # limit to 30FPS 
        time_passed_seconds = time_passed / 1000.0   # convert to seconds

        x, y = pygame.mouse.get_pos()
        a_pos = Vector2D(x, y)

        pygame.draw.rect(screen, (255,255,255), (ra_pos.x, ra_pos.y, ra_sx, ra_sy))
        pygame.draw.rect(screen, (255,255,255), (rb_pos.x, rb_pos.y, rb_sx, rb_sy))
        pygame.draw.circle(screen, (255,255,255), (b_pos.x, b_pos.y), b_radius) # other circle
        pygame.draw.circle(screen, (255,0,0),     (a_pos.x, a_pos.y), a_radius) # mouse

        def draw_vec_from_ball(vec, col):
            """ Draw a vector from the mouse controlled circle. """
            pygame.draw.line(screen, col,  (a_pos.x, a_pos.y), (a_pos.x + vec.x * 20, a_pos.y + vec.y * 20), 3)

        # Draw speed vector
        draw_vec_from_ball(a_speed, (255,255,0))

        # The big rectangle        
        impulse = intersect_rectangle_circle(ra_pos, ra_sx, ra_sy, a_pos, a_radius, a_speed)
        if impulse:
            draw_vec_from_ball(impulse, (0, 255,255))
    
        # The small rectangle
        impulse = intersect_rectangle_circle(rb_pos, rb_sx, rb_sy, a_pos, a_radius, a_speed)
        if impulse:
            draw_vec_from_ball(impulse, (0, 255,255))

        # The circle
        impulse = intersect_circles(a_pos, a_radius, b_pos, b_radius)
        if impulse:
            draw_vec_from_ball(impulse, (0, 255,255))

        pygame.display.update()
    
    
def example2():
    V1 = Vector2D(300, 300)
    V2 = Vector2D(100, 100)

    V3 = V1 + V2

    print(V3)

if __name__ == '__main__':
    example_code()
