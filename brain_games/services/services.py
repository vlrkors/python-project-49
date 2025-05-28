from secrets import SystemRandom

def get_random_number():
    return SystemRandom().randint(1, 100)
