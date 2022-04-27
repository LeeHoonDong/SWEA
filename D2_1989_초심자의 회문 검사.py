def solution(a):
    answer=1
    len_a=len(a)
    i=0
    while i<=len_a//2:
        if a[i]!=a[-1-i]:
            answer=0
            break
        i+=1
    return answer
T=int(input())
for i in range(T):
    a=input()
    answer=solution(a)
    print('#{0} {1}'.format(i+1,answer))