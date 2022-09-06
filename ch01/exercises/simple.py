print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
# the last answer is not rounded at the end correctly

rate = float(input("What is the current exchange rate for Euros to Dollars?"))

amount = float(input("What is the amount of currency you'll be exchanging?"))

total = amount/rate
result = total - 3

print(round(result, 2))

