import timeit

import pyximport

# compile fact.pyx on the fly
pyximport.install()

""" Benchmark Cython vs Python """

print('runtime of cython method even if it s wrote with dynamic typing and pure python {} sec'.format(timeit.timeit('fact.py_fact(20)', setup='import fact', number=1000000)))
print('runtime of pure python executed on python interpreter {} sec'.format(timeit.timeit('interpreted_fact(20)', setup='from factorial.interpreted_fact import interpreted_fact', number=1000000)))

# near two times cython function faster than python func on 1000000 iterations
