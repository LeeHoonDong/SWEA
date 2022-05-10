def solution(a,b):
    if a>=10 or b>=10:
        return -1
    return a*b
TC=int(input())
for i in range(TC):
    a,b=map(int,input().split())
    answer=solution(a,b)
    print('#{0} {1}'.format(i+1,int(answer)))