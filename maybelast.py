def nb_year(p0, percent, aug, p):
    # your code
    
    counter = 0
    while p0 < p :
        p0 += ((percent/100)* p0)+ aug
        counter += 1
    return (counter, p0)



print (nb_year(1000, 2, 50, 1200))

# p0 = 1500000
# percent = 2.5
# aug = 10000
# p = 2000000
# newpeople = 0
# counter = 0
# while  
