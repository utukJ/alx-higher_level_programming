#!/usr/bin/python3

square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
print("=====================\nCompleted square mat simple\n======================")

search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
print("=====================\nCompleted search replace\n======================")

uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
print("=====================\nCompleted uniq add\n======================")

common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
print("=====================\nCompleted common elements\n======================")

only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
print("=====================\nCompleted only diff elements\n======================")
