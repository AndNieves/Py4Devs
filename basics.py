#code conventions: https://www.python.org/dev/peps/pep-0008/

a_variable = 'something that doesnt need type'

a_pair = (1, 2)

first, second = a_pair
print(first, second)

a_list = [0, '1']

a_dictionary = {'key_1': 'value_1', 'key_2': 2}

# iterating a list

for element in a_list:
    print(element)

for index, element in enumerate(a_list):
    print(index, element)

# iterating a dictionary

for key, value in a_dictionary.items():
    print(key, value)

# ranges
print("From 0 to 10")
for i in range(10):
    print(i)

print("From 2 to 8, only pairs")
for i in range(2, 8, 2):
    print(i)

print('while')
i = 2
while i > 0:
    print(i)
    i = i -1

#if
a_boolean_value = True
other_boolean_value = True
yet_another_boolean_value = True

if a_boolean_value or other_boolean_value and yet_another_boolean_value:
    print('Boolean is True')
elif other_boolean_value:
    print('Other Boolean is True')
else:
    print('Nothing is True, everything is a lie!')


# Functions
def a_function_name(some_parameter):
    print(some_parameter)
    return 'some value'


def a_function(parameterA, parameterB):
    print(parameterA, parameterB)
    return parameterA

print(a_function('a', 'b'))

# Lambdas
test_list = [1,2,3,4]

f = lambda x : x + 1

new_list = map(f, test_list)

print('New List')
for element in new_list:
    print(element)
print('Test List')
for element in test_list:
    print(element)

yet_another_new_list = filter(lambda x: x > 2, test_list)
print('Yet another List')
for element in yet_another_new_list:
    print(element)

# Generators
generated_list = [x for x in range(0,10) if x % 2 is 0]
for element in generated_list:
    print(element)

# Slices
slice_list = [x for x in range(1, 10)]
index_2_to_5 = slice_list[2:5]
pairs_2_to_8 = slice_list[2:8:2]
reverse = slice_list[::-1]

#High order
def high_order(f, valueA, valueB):
    f(valueA, valueB)

high_order(a_function, 'A', 'B')

