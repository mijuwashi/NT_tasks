a = [1, 10, 2, 9]
m = sorted(a)[len(a) // 2]
result = sum(abs(v - m) for v in a)
print(result)
