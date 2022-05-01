def solution(s):
    year=s[:4]
    month=s[4:6]
    date=s[6:]
    if 1<=int(month)<=12:
        if int(month)<=7:
            if int(month)==2:
                if 1<=int(date)<=28:
                    return 1
                else:
                    return -1
            elif int(month)%2==0:
                if 1<=int(date)<=30:
                    return 1
                else:
                    return -1
            else:
                if 1<=int(date)<=31:
                    return 1
                else:
                    return -1
        else:
            if int(month)%2==0:
                if 1<=int(date)<=31:
                    return 1
                else:
                    return -1
            else:
                if 1<=int(date)<=30:
                    return 1
                else:
                    return -1
    else:
        return -1
N=int(input())
for i in range(N):
    s=input()
    answer=solution(s)
    year=s[:4]
    month=s[4:6]
    date=s[6:]
    if answer!=-1:
        print('#{0} {1}'.format(i+1,year+'/'+month+'/'+date))
    else:
        print('#{0} {1}'.format(i+1,-1))
    