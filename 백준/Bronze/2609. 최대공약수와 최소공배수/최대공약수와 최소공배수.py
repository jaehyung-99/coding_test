# 유클리드 호제법 사용
n1, n2 = map(int, input().split())
a, b = n1, n2

while(True):
    if a>b:
        a = a%b
        if a == 0:
            print(b)
            print(int(n1*n2/b))
            break
    else:
        b = b%a
        if b == 0:
            print(a)
            print(int(n1*n2/a))
            break