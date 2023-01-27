def solution(s):
    answer = True
    stack = []
    if s[0] == ')' or s[-1] == '(' or len(s)%2 == 1:
        return False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')' and '(' in stack:
            stack.pop()
        else:
            return False
            
    if len(stack) != 0:
        return False
    return True