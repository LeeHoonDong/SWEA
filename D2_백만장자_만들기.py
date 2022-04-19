def solution(arr):
    answer=0
    last=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<last:
            answer+=last-arr[i]
        else:
            last=arr[i]
    return answer
T=int(input())
for i in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    benefit=solution(arr)
    print('#{0} {1}'.format(i+1,benefit))