
def rstar_pyramid():
  rows = int(input("How many rows?"))
  while rows >=0:
    print(rows*"*")
    rows-=1
    
def star_pyramid():
  rows = int(input("How many rows?"))
  for i in range(rows+1):
    print(i*"*")

star_pyramid()
rstar_pyramid() 



