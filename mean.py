array_item = [1,3,2,4]
array_length = len(array_item)

def Math_Median(lst):
    lst.sort()
    length_lst = len(lst)
    if (length_lst % 2 == 0):        
        n = (length_lst - 2) / 2
        convert_n = int(n)
        for i in range(1, convert_n + 1):
            lst.pop(length_lst - i)
        
        for z in range(0, convert_n):
            i = 0
            lst.pop(i)

        value_mean = lst
    
        return value_mean

    elif (length_lst % 2 == 1):
        n2 = (length_lst - 1) / 2
        convert_n2 = int(n2)
        for i in range(1,convert_n2 + 1):
            lst.pop(length_lst - i)
        
        for i in range(0,convert_n2):
            z = 0
            lst.pop(z)
        
        new_lst = lst[0]

        return new_lst


print(Math_Median(array_item))
