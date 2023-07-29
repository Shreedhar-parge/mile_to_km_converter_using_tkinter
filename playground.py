def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(2, 4, 6, 7)

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)




