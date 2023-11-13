import random


def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_numbers(start, end):
    for number in range(start, end + 1):
        if prime_number(number):
            yield number


initial = random.randint(1, 10)
final = random.randint(11, 20)

if __name__ == '__main__':
    primes = list(generate_prime_numbers(initial, final))
    print(f"Прості числа у діапазоні від {initial} до {final}: {', '.join(map(str, primes))}")
