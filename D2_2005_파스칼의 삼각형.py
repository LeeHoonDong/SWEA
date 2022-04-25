def solution(N):
    answer=[[] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(i):
            if i==1 or i==2:
                answer[i].append(1)
            else:
                if j==0 or j==i-1:
                    answer[i].append(1)
                else:
                    answer[i].append(answer[i-1][j-1]+answer[i-1][j])
    return answer

T=int(input())
for i in range(T):
    N=int(input())
    print('#{0}'.format(i+1))
    answer=solution(N)
    for i in range(1,N+1):
        for j in range(i):
            print(answer[i][j],end=' ')
        print()