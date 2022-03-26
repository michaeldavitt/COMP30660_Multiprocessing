import math
import multiprocessing


def my_func(x):
    s = math.sqrt(x)
    return s


def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s
