#조큼 많이 난항을 겪었던 문제
def solution(num):
    answer=[]
    arr=list(num)
    min_num=int(num)
    max_num=int(num)
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):#이중 반복문으로 계속 하나씩 비교: 브루트포스
            temp=arr[:] #temp=arr을 해서 계속 틀렸었음... 차이점이 뭘까?
            if temp[j]!="0" or i!=0:#not(i==0 and temp[j]==0) 이건데, 0이 앞으로 오면 안되니깐
                temp[i],temp[j]=temp[j],temp[i]
                new_num=int("".join(temp))
            #해서 min,max 적용해서 큰값 작은값 알아내기    
            min_num=min(min_num,new_num)
            max_num=max(max_num,new_num)
    answer.append(min_num)
    answer.append(max_num)
    return answer
T=int(input())
for i in range(T):
    num=input()
    answer=solution(num)
    print('#{0} {1} {2}'.format(i+1,answer[0],answer[1]))
