h, m = map(int, input().split())
t = int(input())

# '시' 가 바뀌는 경우
if m+t > 59:
    hour = h+((m+t)//60)
    minute = (m+t)%60
    # '24시' => '0시'
    if hour > 23:
        hour -= 24
    print(hour, minute)
else:
    print(h, m+t)