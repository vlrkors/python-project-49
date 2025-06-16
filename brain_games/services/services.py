from secrets import SystemRandom


def get_random_number():
    
    return SystemRandom().randint(1, 100)


def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
