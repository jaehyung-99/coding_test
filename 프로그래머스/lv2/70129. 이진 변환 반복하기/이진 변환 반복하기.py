def solution(s):
    s_str = str(s)
    cycle = 0
    fc = 0
    while (s_str != '1'):
        cycle += 1
        count = 0
        for i in range(len(s_str)):
            if s_str[i] == '0':
                count += 1
        #count = 0 개수
        fc += count
        s_str = bin(len(s_str)-count)[2:]
    answer = [cycle, fc]
    return answer