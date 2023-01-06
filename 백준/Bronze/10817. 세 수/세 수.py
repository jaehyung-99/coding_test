a, b, c = map(int, input().split())
ans = a
if ans<=b and ans<=c and b<=c:
    ans = b
elif ans<=b and ans<=c and b>=c:
    ans = c
elif ans>=b and ans>=c and b>=c:
    ans = b
elif ans>=b and ans>=c and b<=c:
    ans = c
else:
    ans = a
print(ans)