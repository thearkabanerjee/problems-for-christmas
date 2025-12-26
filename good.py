def spin_words(sentence):
    # Your code goes here
    a = sentence.split()
    lena = len(a)
    
    for i in range (lena):
        if (len(a[i]))>4:
            a[i] = a[i][::-1]

    sentence = ' '.join(a)
    return (sentence)


print(spin_words('Hey fellow warriors'))