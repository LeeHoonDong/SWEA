def solution(arr,n):
    index=[]
    min_answer=int(1e9)
    for start in range(len(arr)):
        if arr[start]==1:
            index.append(start)
    for i in index:
        answer=0
        m=n
        while m>0:
            if i>6:
                i=i%7       
            if arr[i]==1:
                m-=1
            i+=1
            answer+=1
        if min_answer>answer:
            min_answer=answer   
    return min_answer
TC=int(input())
for i in range(TC):
    n=int(input())
    arr=list(map(int,input().split()))
    answer=solution(arr,n)
    print('#{0} {1}'.format(i+1,answer))