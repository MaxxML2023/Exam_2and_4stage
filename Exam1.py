class Container:

    def __init__(self, *instances):
        self.instances = list(instances)

    def all_have_method(self, method_name):
        for instance in self.instances:
            if not hasattr(instance, method_name):
                return False
        return True

# Приклад використання
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"Meow, my name is {self.name}!")

p1 = Person("Alice")
p2 = Person("Bob")
c1 = Cat("Garfield")
c2 = Cat("Felix")

container = Container(p1, p2, c1, c2)

if container.all_have_method("say_hello"):
    print("Всі екземпляри мають метод say_hello")
else:
    print("Не всі екземпляри мають метод say_hello")

if container.all_have_method("meow"):
    print("Всі екземпляри мають метод meow")
else:
    print("Не всі екземпляри мають метод meow")
