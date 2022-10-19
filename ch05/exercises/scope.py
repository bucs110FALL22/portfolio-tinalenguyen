def multiply(x, y):
  res = 0
  if x>y:
    for i in range(y):
      res+=x
  else:
    for i in range(x):
      res+=y
  return res

def exponent(num, expo):
  res = num
  for i in range(expo-1):
    res*=num
  return res

def square(x):
  return exponent(x, 2)

def main():
  print(multiply(2, 3))
  print(exponent(3, 4))
  print(square(7))

main()