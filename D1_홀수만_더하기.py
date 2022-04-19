def solution(arr):
    answer=0
    for number in arr:
        if number%2!=0:
            answer+=number
    return answer
T=int(input())
for i in range(T):
    arr=list(map(int,input().split()))
    sum=solution(arr)
    print('#{0} {1}'.format(i+1,sum))
