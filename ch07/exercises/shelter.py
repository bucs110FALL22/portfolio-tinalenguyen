import time

class Animal:
  def __init__(self, name, type):
    self.id = id(self)
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None 
    self.name = name
    self.type = type

  def set_Adopted(self, manualDate):
    self.adopted = manualDate

  def getID():
    return self.id

  def getDate():
    return self.date

  def getName():
    return self.name


def main():
  meowmeow = Animal("meowmeow", "cat")
  meowmeow.set_Adopted("01/01/2001")

main()