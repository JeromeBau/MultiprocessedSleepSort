import multiprocessing as mp
import time

speed = 0.001
to_be_sorted = [7, 3, 65, 1, 43, 908, 2, 98]

def sort_one_number(x):
    """ Function to be executed by the pool workers"""
    time.sleep(x*speed)
    print(x)
    return x

result_list = []
def log_result(result):
    result_list.append(result)

def apply_async_with_callback():
    pool = mp.Pool()
    for i in to_be_sorted:
        pool.apply_async(sort_one_number, args = (i, ), callback = log_result)
    pool.close()
    pool.join()
    return result_list

apply_async_with_callback()