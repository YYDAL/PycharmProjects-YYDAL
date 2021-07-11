# a = [x for x in []]
# print(a)



def rev_str(my_str):
    length=len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]

for char in rev_str("hello"):
    print(char)

def jisuan(hhh):
    for i in range(length):