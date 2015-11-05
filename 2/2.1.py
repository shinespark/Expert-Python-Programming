# coding: utf-8

# non elegant
size = 10
L = []
i = 0

while i < size:
    if i % 2 == 0 and i != 4:
        L.append(i)
    i += 1

print(L)


# list comprehensions
L = [i for i in range(10) if i % 2 == 0 and i != 4]
print(L)


# unuse enumerate
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    seq[i] = '{0}: {1}'.format(i, element)
    i += 1

print(seq)


# use enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    seq[i] = '{0}: {1}'.format(i, element)

print(seq)


# use enumerate and list comprehensions
def _treatment(pos, element):
    return '{0}: {1}'.format(pos, element)

seq = ['one', 'two', 'three']
print([_treatment(i, el) for i, el in enumerate(seq)])
