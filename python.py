def narcissistic( value ):
    numberofdigits = len(str(value))
    sum = 0
    for i in range (numberofdigits):
        number = (int(str(value)[i])** int(numberofdigits))
        sum += number
         
            
    return (sum == value)