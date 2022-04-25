def solution(N):
    answer=N//3
    return answer
T=int(input())    
for i in range(T):
    N=int(input())
    answer=solution(N)
    print('#{0} {1}'.format(i+1,answer))