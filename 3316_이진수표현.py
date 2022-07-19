def solution(N,M):
    answer="OFF"
    bin_M=format(M,"b")
    if len(bin_M)<N:
        answer="OFF"
    else:
        if "0" in bin_M[len(bin_M)-N:]:
            answer="OFF"
        else:
            answer="ON"
    return answer

TC=int(input())
for tc in range(1,TC+1):
    N,M=map(int,input().split())
    print("#{0} {1}".format(tc,solution(N,M)))