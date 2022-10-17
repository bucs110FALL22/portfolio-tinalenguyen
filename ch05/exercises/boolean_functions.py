def percentage_to_letter(score=0):
  if score>=90:
    return "A"
  if score>=80 and score<90:
    return "B"
  if score>=70 and score<80:
    return "C"
  if score>=60 and score<70:
    return "D"
  else:
    return "F"

def is_passing(letter=None):
  return letter=="C" or letter=="B" or letter=="A"

input = int(input("What is your score?"))

letter = percentage_to_letter(input)
result = is_passing(letter)
print("Passing?", result)