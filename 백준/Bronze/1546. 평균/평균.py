n = int(input())
score_list = list(map(int,input().split()))

M = max(score_list)
total = 0

for i in range(n):
    score_list[i] = score_list[i]/M*100
    total += score_list[i]

ans = total / n
print(ans)