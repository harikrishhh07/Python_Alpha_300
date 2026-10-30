import logging
import json
import random
import secrets
import functools

add10 = lambda x: x + 10
mult = lambda x, y: x * y
a = [1, 2, 3, 4]
b = list(map(lambda x: x*2, a))

try:
    val = 5 / 0
except ZeroDivisionError as e:
    pass
except TypeError as e:
    pass
else:
    pass
finally:
    pass

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('Debug message')
logging.error('Error message')

person = {"name": "John", "age": 30, "city": "New York"}
personJSON = json.dumps(person, indent=4, sort_keys=True)
person_dict = json.loads(personJSON)

rand_a = random.random()
rand_b = random.randint(1, 10)
rand_c = secrets.randbelow(10)

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add5(x):
    return x + 5

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)