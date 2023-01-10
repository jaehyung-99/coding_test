import sys
n = int(sys.stdin.readline())
count = 0
temp = n
while(True):
    if(n%5 == 0):
        print(n//5)
        break
    else:
        if(temp<3):
            print(-1)
            break
        else:
            temp -= 3
            count += 1
            if (temp%5 == 0):
                print(count + temp//5)
                break