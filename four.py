string_variable = "Loop-de-loop"

# for loops in Python follow this pattern:
# for <variable> in <iterable>:
#     ... do something with variable

# for each_letter in string_variable:
#     print(each_letter)

# a new data type approaches! lists, which look a lot like JavaScript's arrays
my_list = [1, 2, 3, "four"]

# for item in my_list:
#     print(item)

new_list = [1, 2, 3, ["meta list", "list within a list", ["super inception"]]]

# the index of the list is used to access the data
print(new_list[3][2][0])

# python also has while loops

i = 0
while i <= 10:
    print("i am at", i)
    i = i + 1
