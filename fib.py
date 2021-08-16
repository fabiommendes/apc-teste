n = int(input("n: "))
x, y = 1, 1
fibs = []

for _ in range(n):
    fibs.append(x)
    x, y = y, x + y
  
print(fibs)
