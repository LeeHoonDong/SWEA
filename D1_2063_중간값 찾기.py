def solution(N,arr):
    answer=0
    arr.sort()
    len_arr=len(arr)
    answer=arr[len_arr//2]
    print(answer)
    return answer
N=int(input())
arr=list(map(int,input().split()))
solution(N,arr)