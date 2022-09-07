import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("Cost per week:", cost_per_week)
print("This is the cost per class: ", cost_per_class) 

#Part B

myList = [42, "beep", 24.25, "howdy!", "boo"]
result = random.choice(myList)
print("Result from random choice:", result)