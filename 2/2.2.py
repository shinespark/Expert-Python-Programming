# coding: utf-8
class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Returns the next element."""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    __next__ = next  # for python3.x

    def __iter__(self):
        """Returns the iterator itself."""
        return self

for el in MyIterator(4):
    print(el)


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


def power(values):
    for value in values:
        print('powering {0}'.format(value))
        yield value


def adder(values):
    for value in values:
        print('adding to {0}'.format(value))
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1, 4, 7, 9, 12, 19]
res = adder(power(elements))
print(next(res))
print(next(res))
print(next(res))
print(next(res))


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = yield
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("A that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")


free = psychologist()
next(free)
free.send('I feel bad')
free.send('I feel good')
free.send("Why I shouldn't?")
