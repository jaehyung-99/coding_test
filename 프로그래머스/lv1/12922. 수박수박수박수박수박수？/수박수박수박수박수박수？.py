def solution(n):
    
    if n%2 == 0:
        answer = "수박"*(n//2)
        return answer
    else:
        answer = "수"+"박수"*(n//2)
        return answer