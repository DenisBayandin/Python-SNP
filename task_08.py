def multiply_numbers(inputs=''):
    if inputs=='':
        return None
    proverka = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,[] '
    output = 1
    if type(inputs) != str:
        inputs = str(inputs)
    for i in inputs.upper():
        if i in proverka:
            continue
        else:
            output*=int(i)
    if output==1:
        return None
    else:
        return output

multiply_numbers()  #--> None
multiply_numbers('ss')  #--> None
multiply_numbers('1234')  #--> 24
multiply_numbers('sssdd34')  #--> 12
multiply_numbers(2.3)  #--> 6
multiply_numbers([5, 6, 4])  #--> 120




