def interpreted_fact(n):
    """Computes n!"""
    if n <= 1:
        return 1

    return n * interpreted_fact(n - 1)
