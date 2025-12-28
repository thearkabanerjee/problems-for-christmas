s = 'abcd'
li = []
if len(s)%2 == 0:
    for i in range (1,len(s)):
       print (s[i-1]+s[i])