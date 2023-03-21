def alphbetize(original_list=[]):
    sorted_list = original_list.copy()

    sorted_list.sort()
    final_list = ''

    for name in sorted_list:
        final_list += name +', '
    
    final_list = final_list[:-2]

    print(final_list)

names = ['Ravi','Teja','Kiran','Divya']

alphbetize(names)