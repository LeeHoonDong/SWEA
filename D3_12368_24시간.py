def solution(A,B):
    answer=A+B
    if answer>=24:
        answer-=24
    return answer
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    answer=solution(A,B)
    print('#{0} {1}'.format(i+1,answer))