from rectangle import *

class Surface:
  
  def __init__(self, filename, x, y, h, w):
    '''
      This function is a constructor for the Surface class.
      args: (obj) self, (str) filename, (int) x, (int) y, (int) h, (int) w
      returns: None
    '''
    self.image = filename
    self.rect = Rectangle(x, y, h, w)

  def getRect(self):
    '''
      This function returns the rectangle object. 
      args: (obj) self
      returns: internal rectangle object
    '''
    return self.rect