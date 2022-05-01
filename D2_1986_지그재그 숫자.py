def solution(N):
    answer=0
    for i in range(1,N+1):
        if i%2==1:
            answer+=i
        else:
            answer-=i
    return answer
T=int(input())
for i in range(T):
    N=int(input())
    answer=solution(N)
    print('#{0} {1}'.format(i+1,answer))