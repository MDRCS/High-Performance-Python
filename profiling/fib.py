import cProfile


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


print('Fib Recursion')
print('=' * 80)

cProfile.runctx('fib(20)',globals(),locals())

print('Fib Sequential')
print('=' * 80)

cProfile.runctx('fib_seq(20)', globals(), locals())

"""
As you can see, it takes 57356 separate function calls and 3/4 of a second to run.
Since there are only 66 primitive calls, we know that the vast majority of those 57k calls were recursive.
The details about where time was spent are broken out by function in the listing showing the number of calls,
total time spent in the function, time per call (tottime/ncalls), cumulative time spent in a function,
and the ratio of cumulative time to primitive calls.
"""
