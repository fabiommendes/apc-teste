n = int(input("n: "))
fibs = [1, 1]

while len(fibs) < n:
    fibs.append(fibs[-1] + fib[-2])

print("Sequência de Fibonacci")
print(fibs)
