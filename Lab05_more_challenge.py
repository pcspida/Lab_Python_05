# Problem 8
def binary(num):
    base2=0
    i=0
    while num>0:
        base2=base2+num%2*(10**i)
        num/=2
        i+=1
    return base2 
print binary(6)

# Problem 9
