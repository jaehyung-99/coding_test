ans = list(range(1,10001))
for i in range(1,10001):
    target = i + (i//1000 + (i//100)%10 + (i//10)%10 + i%10)
    if target in ans:
        ans.remove(target)
for i in ans:
    print(i)