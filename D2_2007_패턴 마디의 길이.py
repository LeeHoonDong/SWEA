def solution():
    answer=0
    sentence=input()
    i=1
    while i<len(sentence):
        if sentence[:i+1]==sentence[i+1:2*i+2]:
            answer=len(sentence[:i+1])
            break
        i+=1
    return answer
T=int(input())
for i in range(T):
    answer=solution()
    print('#{0} {1}'.format(i+1,answer))
