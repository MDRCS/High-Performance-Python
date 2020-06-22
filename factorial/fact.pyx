def py_fact(n):
    """Computes n!"""
    if n <= 1:
        return 1
    return n * py_fact(n - 1)

def typed_fact(long n):
    """Computes n!"""
    if n <= 1:
        return 1
    return n * typed_fact(n - 1)

