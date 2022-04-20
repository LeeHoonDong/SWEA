T=int(input())
for i in range(T):
    m,n=map(int,input().split())
    if m<n:
        print('#{0} {1}'.format(i+1,"<"))
    elif m==n:
        print('#{0} {1}'.format(i+1,"="))
    else:
        print('#{0} {1}'.format(i+1,">"))