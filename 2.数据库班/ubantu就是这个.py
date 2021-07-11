m = []
for a in range(1, 101):
    if a % 7 == 0 or a // 10 == 7:
        pass
    else:
        m.append(a)
print(m)
