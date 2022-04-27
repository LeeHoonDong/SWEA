T=int(input())
answer=[]
for i in range(T):
    A,B,C,D=map(int,input().split())
    if B<=C:
        answer.append(0)
    else:#B>C
        if B<D:
            if A>=C:
                answer.append(B-A)
            else:
                answer.append(B-C)
        else:
            if A>=C:
                answer.append(D-A)
            else:
                answer.append(D-C)
for i in range(T):
    print('#{0} {1}'.format(i+1,answer[i]))