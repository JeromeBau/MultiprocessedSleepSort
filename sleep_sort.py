import multiprocessing as mp
import time

results = []


def sort_one_number(x, speed):
    """ Function to be executed by the pool workers"""
    time.sleep(x*speed)
    return x


def save_results(result):
    results.append(result)


def start_sorting(to_be_sorted, speed=0.001):
    pool = mp.Pool()
    for i in to_be_sorted:
        pool.apply_async(sort_one_number, args=(i, speed, ), callback=save_results)
    pool.close()
    pool.join()
    return results

