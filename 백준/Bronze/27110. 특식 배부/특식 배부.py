n = int(input())
list = list(map(int,input().split()))
ans = 0

for i in list:
    if i>n:
        ans += n
    else:
        ans += i
print(ans)