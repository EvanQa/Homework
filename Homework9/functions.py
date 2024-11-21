#exercise 1
#1
def add_numbers(a, b):
    return a + b
result = add_numbers(2, 3)
print(result)
#2
def subtract_numbers(a, b):
    return a - b
result = subtract_numbers(5, 1)
print(result)
#3
def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(2, 10)
print(result)
#4
def divide_numbers(a,b):
    return a / b
result = divide_numbers(6, 2)
print(result)

#exercise 2
def print_parameters(name, age, height):
    print(f"Name : Type = {type(name)}, Value = {name}" )
    print(f"Age : Type = {type(age)}, Value = {age}" )
    print(f"Height : Type = {type(height)}, Value = {height}" )

print(print_parameters("Ivan",23,1.85))

#exercise 3
def combine_string(str1, str2, str3):
    return str1 + str2 + str3
result = combine_string("Print", " Hello ", "World!")
print(result)

#exercise 4
