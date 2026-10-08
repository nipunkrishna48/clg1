def is_prime(number: int) -> bool:
    """Return whether number is prime; only integers are accepted."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


if __name__ == "__main__":
    examples = (2, 17, 1, 0, -5, 21)
    for value in examples:
        print(f"{value}: {'prime' if is_prime(value) else 'not prime'}")
