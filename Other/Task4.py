# Decorator itself
def process_list(original_list, x):
    buffer_list = []
    new_list = []
    for lists in original_list:
        buffer_list.append(lists)
        print(buffer_list)
    for i in buffer_list:
        i = i - x
        new_list.append(i)

    def decorator(original_func):
        return original_func(new_list)
    return decorator

# Task 2


def filter_list(one_d_list):
	filtered = []

	for item in one_d_list:
		if 100 >= item >= 10:
			filtered.append(item)

	mean_value = sum(filtered) / len(filtered)
	min_value = min(filtered)
	max_value = max(filtered)
	sum_of_values = sum(filtered)
	return mean_value, min_value, max_value, sum_of_values


def filter_two_d_list(two_d_list):

	for obj in two_d_list:
		filtered = filter_list(obj)
		print(filtered)


# Variables
filter_two_d_list([
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
])

# Implementation of decorator
decorated = process_list(filter_two_d_list, 10)
decorated([
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
])
