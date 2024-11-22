def apply_all_func(int_list, *functions):
    results = dict() 
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

def min_int(int_list1):
    return min(int_list1)

def max_int(int_list2):
    return max(int_list2)

def len_int(int_list3):
    return len(int_list3)

def sum_int(int_list4):
    sum(int_list4)

def sorted_int(int_list5):
    sorted(int_list5)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))