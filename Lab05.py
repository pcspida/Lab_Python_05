'''
Kwabena Ansah
Solution File Lab05
'''
#Problem 2
def factorial(num):
    if(num<=0):
        return 1
    else:
        return num*factorial(num-1)
print 'The factorial is',factorial(5)

#Problem 3
def fibonacci(count):
    result = []
    a,b = 0,1
    n_times = 0
    while n_times != count:
        result.append(b)
        a,b = b, a + b
        n_times += 1
    return result
        
fib_test = fibonacci(5)
print 'The fibonacci numbers are %s'%(fib_test)


#Problem 4
def prime(num):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0 or num == 1:
            prime=False
            break
    return prime
print prime(9)

#Problem 5
def isPalindrome(st):
    return st == st[::-1]

print isPalindrome("able was I ere I saw elba")

#Problem 6
def isSubstring(phrase1,phrase2):
    substring=False
    length1=len(phrase1)
    length2=len(phrase2)
    lim=length2-length1+1
    for i in range(lim):
        temp=phrase2[i:length1+i]
        if phrase1==temp:
            substring=True
            break

    return substring

print isSubstring('bar','foobar')
            
#Problem 7
def maxScore(me,Fred,Jill):
    score=0
    length=len(me)
    for i in range(length):
        if me[i]!=Fred[i] or me[i]!=Jill[i]:
            if Fred[i]==Jill[i]:
                score+=2
            else:
                score+=1
    return score

print maxScore('AAABCDA','ADDBACA','ADCADDC')
