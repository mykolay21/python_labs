# Python program to check if two
# to get unique values from list
# using traversal

# function to get unique values
def unique(list1, list2):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
# check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
        # print list
    for y in list2:
        if y not in unique_list:
            unique_list.append(y)

    print(unique_list)

    # driver code

"""
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("the unique values from 1st list is")
unique(list1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("\nthe unique values from 2nd list is")
unique(list2)
"""
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unique(list1, list2)






def common_data(lista, listb):
    is_in_both = []

    # traverse in the 1st list
    for x in lista:

        # traverse in the 2nd list
        for y in listb:

            # if one common
            if x.__eq__(y):
                is_in_both.append(y)

    print(is_in_both.sort())


lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_data(lista, listb)



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def common(a,b):
    c = [value for value in a if value in b]
    return c

print(common(a, b))


# 2-nd variant
a2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common(a, b))

# 3-d variant

a3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a3).intersection(b3)))
print(list(set(a3) & set(b3)))

# Task 2

def solution(long_str, short_str):
   # implement function here
    result = long_str.endswith(short_str)
    print(result)


# Testcases
solution('abc', 'bc')  # returns True
solution('abc', 'd')  # returns False
solution('abc', 'dikikik')  # returns False
solution('abc', 'abc')  # returns True


