n = int(input())
ans_list = []
for i in range(n):
    s_list = list(map(int,input().split()))
    avg = (sum(s_list) - s_list[0]) / s_list[0]
    count = 0
    for i in range(len(s_list)-1):
        if s_list[i+1] > avg:
            count += 1
    ans = count/s_list[0]*100
    ans = f"{ans:.3f}%"
    ans_list.append(ans)
for i in range(n):
    print (ans_list[i])