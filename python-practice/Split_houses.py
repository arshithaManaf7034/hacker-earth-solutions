n = int(input())  
s = input().strip()


flag = False
for i in range(n-1):
    if s[i] == 'H' and s[i+1] == 'H':
        flag = True
        break
if flag == True:
    print('NO')
else:
    print('YES')
    res = ''
    for j in s:
        if j =='.':
            res = res+'B'
        else:
            res = res+'H'
    print(res)
               
