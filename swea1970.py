def solution(money):
    answer=[]
    dict={50000:0, 10000:0,5000:0,1000:0,500:0,100:0,50:0,10:0}
    for key in dict.keys():
        dict[key]=money//key
        money=money%key
    for value in dict.values():
        answer.append(value)
    return answer
Test_case=int(input())
for i in range(1,Test_case+1):
    money=int(input())
    answer=solution(money)
    print("#{0}".format(i))
    for j in range(len(answer)):
        print(answer[j],end=" ")
    print()