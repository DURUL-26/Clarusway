fibonacci = [0, 1]
for i in range(0, 9):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
fibonacci.pop(0)
print("fibonacci->", fibonacci)
