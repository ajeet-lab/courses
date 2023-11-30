#In Python, a set is an unordered collection of unique elements. It is a data structure that is used to store multiple items, but unlike lists or tuples, it does not allow duplicate values. Sets are defined using curly braces {} or the set() constructor.


# num = {10, 20 , 10, 13}
# print(num)

num1 = set([1, 2, 3, 4, 1,3])
num1.add(20) ## Adding elements to a set
num1.remove(3) ## Removing elements from a set
print(num1)