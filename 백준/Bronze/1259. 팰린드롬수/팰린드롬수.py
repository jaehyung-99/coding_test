ans_list = []
while(True):
    word = input()
    bo = True
    count = 0
    if word == '0':
        break
    elif word == '1':
        ans_list.append('yes')
    else:
        for i in range(len(word)):
            count += 1
            if word[i] != word[len(word)-count]:
                bo = False
                break
        if bo == True:
            ans_list.append('yes')
        else:
            ans_list.append('no')
for i in ans_list:
    print(i)