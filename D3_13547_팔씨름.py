def solution(arr):
    answer=''
    sojung=0
    sejung=0
    for alpha in arr:
        if alpha=='o':
            sojung+=1
        else:
            sejung+=1
    remain=15-len(arr)
    if remain+sojung>=8:
        answer='YES'
    else:
        answer='NO'
    return answer
T=int(input())
for i in range(T):
    arr=list(input())
    answer=solution(arr)
    print('#{0} {1}'.format(i+1,answer))