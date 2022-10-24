class Player:
  def __init__(self):
    	'''
			Initialize the player object
               
               args: pnum [int] the player's id number  
		'''
    self.health = 100 #player health
    self.points = 0 #player starts with no points
    self.isMoving = False #player starts standing still

class Goomba:
  def __init__(self):
    ''' Initialize the Goombas '''
    self.health = 20 #goomba health
    self.isMoving = True #goomba is moving
    self.touchesPlayer = False #turns true when goomba touches player

class Mysterybox:
  def __init__(self):
    ''' Initialize the mystery boxes '''
    self.isTouched = False #turns true when player touches the box
    self.Health = 5 #box health
    self.prize = 10 #number of points the box contains
