def connect_dicts(dict1, dict2):
    sum_value_2 = 0
    sum_value = 0
    new_dict = {}
    new_sorted_dict = {}
    for key, value in dict1.items():
        sum_value += value
    for key_2, value_2 in dict2.items():
        sum_value_2+=value_2
    if sum_value>sum_value_2:
        for key, value in dict1.items():
            if value>=10:
                new_dict[key]=value
        for key_2, value_2 in dict2.items():
            if key_2 in new_dict:
                continue
            else:
                if value_2>=10:
                    new_dict[key_2]=value_2
    else:
        for key_2, value_2 in dict2.items():
            if value_2>=10:
                new_dict[key_2]=value_2
        for key, value in dict1.items():
            if key in new_dict:
                continue
            else:
                if value>=10:
                    new_dict[key]=value
    new_not_sorted_dict = sorted(new_dict, key=new_dict.get)
    for i in new_not_sorted_dict:
        new_sorted_dict[i] = new_dict[i]
    return new_sorted_dict

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })  #--> {'c': 11, 'b': 12}
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })  #--> {'d': 11, 'c': 12, 'a': 13}
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })  #--> {'c': 11, 'b': 12, 'a': 15}