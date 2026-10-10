def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two natural numbers."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two natural numbers."""
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b


def square(x: int) -> int:
    """Return the square of a number."""
    return x * x

