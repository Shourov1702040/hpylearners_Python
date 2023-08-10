def my_fucntion(a,b,c):
    max=0
    min=0

    if a>b and a>c:
        max = a 
    elif b>a and b>c:
        max = b 
    else: 
        max = c

    if a<b and a<c:
        min = a 
    elif b<a and b<c:
        min = b 
    else: 
        min = c
    
    return max, min
max, min = my_fucntion(7,9,1)
# print("Maximum = ",max)
# print("Minimum = ",min)

# n = 0
# for i in range(11):
#     n = n+i
# print(n)

def recursive(n):
    if n==1:
        return 1
    else:
        return n+recursive(n-1)

sum = recursive(10)
# print(sum)