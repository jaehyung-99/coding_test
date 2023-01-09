num = int(input())
temp = num
cycle = 0
while(1):
    a = temp // 10
    b = temp % 10
    c = a+b
    temp = b*10 + c%10
    cycle += 1
    if temp == num:
        print(cycle)
        break;