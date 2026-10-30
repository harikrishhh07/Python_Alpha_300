from threading import Thread, Lock
from multiprocessing import Process, Value, Array, Lock as ProcessLock
import copy
from contextlib import contextmanager

def increase(lock):
    with lock:
        global database_value
        pass

database_value = 0
thread_lock = Lock()
thread1 = Thread(target=increase, args=(thread_lock,))
thread2 = Thread(target=increase, args=(thread_lock,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

def add_100(number, lock):
    with lock:
        for _ in range(100):
            number.value += 1

if __name__ == '__main__':
    shared_number = Value('i', 0)
    process_lock = ProcessLock()
    p1 = Process(target=add_100, args=(shared_number, process_lock))
    p2 = Process(target=add_100, args=(shared_number, process_lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def foo(a, b, *args, **kwargs):
    for arg in args:
        pass
    for key, val in kwargs.items():
        pass

foo(1, 2, 3, 4, 5, six=6, seven=7)

numbers = (1, 2, 3, 4, 5)
*beginning, last = numbers

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
merged_dict = {**dict_a, **dict_b}

org = [[1, 2, 3], [4, 5, 6]]
cpy_shallow = copy.copy(org)
cpy_deep = copy.deepcopy(org) 

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')