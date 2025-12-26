def get_sum(a,b):
    #good luck!
    sum = 0
    if a > b :
        smallernum = b
        greaternum = a
    else:
        smallernum = a
        greaternum = b

    if a!=b :
        for i in range(smallernum, greaternum+1):
            sum += i
            
        return (sum)
    else:
        return (a)
    
print(get_sum (-1, 2))




