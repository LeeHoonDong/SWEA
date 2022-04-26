def solution(arr,N,M):
    answer=0
    result=0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            for a in range(M):
                for b in range(M):
                    result+=arr[i+a][j+b]
            if answer<result:
                answer=result
            result=0
    return answer
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    arr=[]
    for j in range(N):
        arr.append(list(map(int,input().split())))
    answer=solution(arr,N,M)
    print('#{0} {1}'.format(i+1,answer))