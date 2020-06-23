# distutils: sources=["mt19937ar.c"]
# cython: language_level=3
cimport mt

def init_state(unsigned long s):
    mt.init_genrand(s)

def rand():
    return mt.genrand_real1()
