def solution(arr):
    answer=0
    sum=0
    length=len(arr)
    arr.sort()
    print(arr)
    for i in range(1,length-1):
        sum+=arr[i]
    answer=sum/(length-2)
    return round(answer,0)

T=int(input())
for i in range(T):
    arr=list(map(int,input().split()))
    answer=solution(arr)
    print('#{0} {1}'.format(i+1,answer))