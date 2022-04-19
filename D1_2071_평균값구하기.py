def solution(arr):
    answer=0
    for num in arr:
        answer+=num
    answer=answer/len(arr)
    return round(answer)

T=int(input())
for i in range(T):
    arr=list(map(int,input().split()))
    sum=solution(arr)
    print('#{0} {1}'.format(i+1,sum))
