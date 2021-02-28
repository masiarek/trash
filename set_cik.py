a = [9, 7, 7]
b = [7, 8]
s = set(a)
s2 = set(tuple((a, b) for a in range(2)) for b in range(5))

c = set(a + b)
print(c)
