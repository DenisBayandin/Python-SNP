def sort_list(list=[]):
    temporary_list = []
    if list==[]:
        return temporary_list
    else:
        m = 0
        n = list[0]
        for i in list:
            if i >= m:
                m = i
            if n >= i:
                n = i
        for j in list:
            if j == m:
                temporary_list.append(n)
            elif j == n:
                temporary_list.append(m)
            else:
                temporary_list.append(j)
        temporary_list.append(n)
        return temporary_list

sort_list([])  #--> []
sort_list([2, 4, 6, 8])  #--> [8, 4, 6, 2, 2]
sort_list([1])  #--> [1, 1]
sort_list([1, 2, 1, 3])  #--> [3, 2, 3, 1, 1]