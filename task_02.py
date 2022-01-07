def coincidence(list, range):
    if list=='' and range=='':
        return []
    for i in list:
        for j in range:
            if type(i)==float:
                if j<i<i+1:
                    list_1.append(i)
                    break
            elif type(i)==int:
                if i==j:
                    list_1.append(i)
                    break
    return list_1

list_1=[]
coincidence([1, 2, 3, 4, 5], range(3, 6))    #--> [3,4,5]
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))   #-->[1,2,2.5]
coincidence(list='',range='')   #-->[]
