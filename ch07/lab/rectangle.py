class Rectangle:
  def __init__(self, x, y, h, w):
    '''
      This function is a constructor for the Rectangle Class.
      args: (obj) self, (int) x, (int) y, (int) h, (int) w
      returns: None
    '''
    newArray=[]
    for element in [x, y, h, w]:
      if element < 0:
        newArray.append(0)
      else:
        newArray.append(element)

    self.x = newArray[0]
    self.y = newArray[1]
    self.height = newArray[2]
    self.width = newArray[3]

  def __str__(self):
    '''
      This function returns a string containing the x, y, width, and height of the rectangle.
      args: (obj) self
      returns: a string containing the x, y, width, and height of the rectangle
  
    '''
    return "x:"+str(x)+", y:"+str(y)+", height:"+str(h)+", width:"+str(w)

  


