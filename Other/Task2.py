
def filter_list(one_d_list):
	filter(lambda num: 10 <= num <= 100, one_d_list)
	mean_value = sum(one_d_list) / len(one_d_list)
	min_value = min(one_d_list)
	max_value = max(one_d_list)
	sum_of_values = sum(one_d_list)
	return mean_value, min_value, max_value, sum_of_values


def filter_two_d_list(two_d_list):

	for obj in two_d_list:
		filter_list(obj)
		print(obj)


# print(filter_list([1, 10, 34, 110, 400, 30, 20, 100, 101, 9, 11, 10]))
filter_two_d_list([
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
])
