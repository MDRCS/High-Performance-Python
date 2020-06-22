import timeit

import pyximport

# compile fact.pyx on the fly
pyximport.install()

""" Benchmark Cython vs Python """

print('runtime of cython method even if it s wrote with dynamic typing and pure python {} sec'.format(timeit.timeit('fact.py_fact(20)', setup='import fact', number=1000000)))
print('runtime of pure python executed on python interpreter {} sec'.format(timeit.timeit('interpreted_fact(20)', setup='from factorial.interpreted_fact import interpreted_fact', number=1000000)))

# near two times cython function faster than python func on 1000000 iterations

print('runtime of cython with statical typing and pure python {} sec'.format(timeit.timeit('fact.typed_fact(20)', setup='import fact', number=1000000)))

"""
runtime of cython method even if it s wrote with dynamic typing and pure python 1.7897053609999998 sec
runtime of pure python executed on python interpreter 3.825792878 sec
runtime of cython with statical typing and pure python 1.4818592860000006 sec
"""


# we can observe that statically typing variables will enhance performance of our cython func from this 1.7897053609999998 sec to this 1.4818592860000006 sec.



