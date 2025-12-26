def solution(text, ending):
    # your code here...
    endingnumber = len(ending)
    
    return (text[-endingnumber:]== ending)
   


print(solution('text', 'xt'))


