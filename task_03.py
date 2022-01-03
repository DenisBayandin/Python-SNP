def max_odd(array):
    m = 0
    for i in array:
        if type(i)==int or type(i)==float:
            if i%2!=0:
                if i>=m:
                    m=i
    if m==0:
        return None
    else:
        return int(m)

max_odd([1, 2, 3, 4, 4])  #--> 3
max_odd([21.0, 2, 3, 4, 4])  #--> 21
max_odd(['ololo', 2, 3, 4, [1, 2], None])  #--> 3
max_odd(['ololo', 'fufufu'])  #--> None
max_odd([2, 2, 4])  #--> None