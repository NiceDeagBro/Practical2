import Task2

def decorator(func, x):
    def func_arg(arg):
        result = func(arg)
        for item in arg:
            item = item - x
        return result
    return(func_arg)

# print decorated output of function "filter_list" of Task2 
print(decorator(Task2.filter_list([1, 10, 34, 110, 400, 30, 20, 100, 101, 9, 11, 10]), 10))
