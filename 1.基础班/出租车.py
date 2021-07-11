a = int(input('输入你的路程'))
way = a
if a < 3:
    print('10')
elif 3 <= a < 20:
    print(str((a-3)*3+10))
else:
    print(float(a-20)*3.6+61)