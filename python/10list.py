
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers); #Print all nunbers
print(numbers[4]); #Print value using index
print(numbers[2:8]); #Print value in range [start:end]

numbers.append(10) # Append value in end
print(numbers)

numbers.insert(3, 11) # Insert value at index(indexNumber, insertValueAtNumber)
print(numbers)
print(len(numbers)) #Find length of list
print(10 in numbers)