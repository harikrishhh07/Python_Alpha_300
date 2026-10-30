my_list = ["banana", "cherry", "apple"]

a = my_list[1:5]
reversed_list = my_list[::-1]

numbers = [1, 2, 3, 4, 5, 6]
squared = [i*i for i in numbers]

my_tuple = ("Max", 28, "Boston")

name, age, city = my_tuple

my_tuple2 = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple2

my_dict = {"name": "Max", "age": 28, "city": "New York"}

my_dict["email"] = "max@xyz.com"
my_dict.update({"name": "Mary", "age": 27})

for key, value in my_dict.items():
    print(key, value)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
i = odds.intersection(primes)
diff = odds.difference(primes)

var = "Tom"
new_string = f"The variable is {var}"

my_string_list = ['How', 'are', 'you', 'doing']
joined_string = ' '.join(my_string_list)

from collections import Counter, namedtuple, defaultdict, deque

my_counter = Counter("aaaaabbbbccc")
print(my_counter.most_common(1))

Point = namedtuple('Point', 'x y')
pt = Point(1, -4)

from itertools import product, permutations, combinations, groupby

a_iter_list = [1, 2, 3]
perm = permutations(a_iter_list)
comb = combinations(a_iter_list, 2)
prod = product(a_iter_list, [4, 5])