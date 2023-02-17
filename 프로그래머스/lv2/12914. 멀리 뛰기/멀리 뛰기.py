def solution(n):
    a,b = 1,2
    if n==1:
        return 1
    elif n==2:
        return 2
        
    for i in range(1,n):
        a,b = b, a+b

    return a%1234567