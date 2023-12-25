def fctrl(num):
    sum = 1
    for i in range(1, num+1):
        sum = sum * i
    return sum

def sqfctrl(num):
    sqsum = 0
    for i in range(1, num+1):
        sqsum = sqsum + fctrl(i)
    return sqsum

print(sqfctrl(int(input("--"))))
