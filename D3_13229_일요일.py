def solution():
    answer=0
    hash_date={'MON':0,"TUE":1,"WED":2,"THU":3,"FRI":4,"SAT":5,"SUN":6}
    date=input()
    if date=="SUN":
        answer=7
    else:
        answer=hash_date["SUN"]-hash_date[date]
    return answer
T=int(input())
for i in range(T):
    answer=solution()
    print('#{0} {1}'.format(i+1,answer))