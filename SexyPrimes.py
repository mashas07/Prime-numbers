def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def find_sexy_primes(limit):
    sexy_primes = []

    for p in range(2, limit - 5):
        if is_prime(p) and is_prime(p + 6):
            sexy_primes.append((p, p + 6))

    return sexy_primes

N = int(input("Enter the value of N: "))
print("Sexy primes up to", N)
sexy_primes = find_sexy_primes(N)

import matplotlib.pyplot as plt
import numpy as np
import sympy
import math

# plt.style.use('dark_background')

def get_coordinate(num, deg_sep):
    radius = num
    omega = deg_sep * np.pi/360
    return radius * np.cos(omega * num), radius * np.sin(omega * num)

def create_plot2(nums, figsize=8, s=None, show_annot=False):
    nums = np.array(sexy_primes)
    x, y = get_coordinate(nums, 2)
    plt.figure(figsize=(figsize, figsize))
    plt.axis("off")
    plt.scatter(x, y, s=s, color = '#DE7691')
    plt.show()

create_plot2(sexy_primes, s=5)