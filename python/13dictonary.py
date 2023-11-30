#In Python, a dictionary is a built-in data structure that allows you to store and retrieve key-value pairs. Dictionaries are sometimes referred to as associative arrays or hash maps in other programming languages. Here's an overview of how to work with dictionaries in Python

student = {"name": "John", "age": 30, "city": "New York"}
print(student.get("name"))
print(student["name"])

student["name"]="abc" #Update the name
print(student["name"])

student["gender"]="Male" #Add a new key-value pair
print(student)
del student["city"] # Remove the "city" key-value pair

print(student)


# Iterating through keys
for key in student:
    print(key)

# Iterating through values
for value in student.values():
    print(value)

# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)