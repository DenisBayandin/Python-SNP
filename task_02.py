def coincidence(list='', range=''):
    list_new = []
    if list == '' and range == '':
        return list_new
    for i in list:
        for j in range:
            if type(i) == int:
                if i == j:
                    list_new.append(i)
            if type(i) == float:
                if j<i<j+1:
                    list_new.append(i)
    return list_new

coincidence([1, 2, 3, 4, 5], range(3, 6))  # --> [3, 4, 5]
coincidence()  # --> []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))  # --> [1, 2, 2.5]
