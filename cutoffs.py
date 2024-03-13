import math

xs = [239, 1023, 5832, 110443, 4841182, 6826318]

def f(x, y):
    terms = math.log(10, x) * y / 2
    return math.ceil(terms) + 2

for i in range(1, 6):
    fs = [str(f(x, 10**i)) for x in xs]
    print(f"{i} & {' & '.join(fs)} \\\\")
