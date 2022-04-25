def solution():
    answer=0
    arr=list(map(int,input().split()))
    answer=max(arr)
    return answer
T=int(input())
for i in range(T):
    answer=solution()
    print('#{0} {1}'.format(i+1,answer))