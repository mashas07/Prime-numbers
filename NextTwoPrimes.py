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

def find_twin_primes(N):
    twin_primes = []
    midpoint = []
    for num in range(2, N + 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
            # midpoint.append(num+1)
    return twin_primes

def find_allprimes(N):
    allprimes = []
    for num in range(2, N + 1):
        if is_prime(num):
            allprimes.append(num)
        # midpoint.append(num+1)
    return allprimes

N = int(input("Enter the value of N: "))
print("Twin primes up to", N)
twin_primes = find_twin_primes(N)
for prime_pair in twin_primes:
    prime1, prime2 = prime_pair
    print(str(prime1)+ ", "+str(prime2))

allprimes = find_allprimes(N)

import matplotlib.pyplot as plt
import numpy as np
import sympy
import math

# plt.style.use('dark_background')

def get_coordinate(num, deg_sep):
    radius = num
    omega = deg_sep * np.pi/360
    return radius * np.cos(omega * num), radius * np.sin(omega * num)

def get_coordinate_new(num, deg_sep):
    radius = num
    omega = deg_sep * np.pi/360
    theta = omega * num
    x, y = radius * np.cos(omega * num), radius * np.sin(omega * num)
    dx = 3*N/180
    dx, dy = -np.sin(theta) * dx, np.cos(theta) * dx
    return((x + dx, x - dx), (y + dy, y-dy))

# def create_plot(nums, figsize=8, s=None, show_annot=False):
#     nums = np.array(nums)
#     nums = nums.T[0] + 1
#     # x, y = get_coordinate(nums, 2)
#     x, y = get_coordinate_new(nums, 2)
#     x, y = np.array(x).flatten(), np.array(y).flatten()
#     plt.figure(figsize=(figsize, figsize))
#     plt.axis("off")
#     plt.scatter(x, y, s=s)

# def create_plot2(nums, figsize=8, s=None, show_annot=False):
#     nums = np.array(nums)
#     x, y = get_coordinate(nums, 2)
#     plt.figure(figsize=(figsize, figsize))
#     plt.axis("off")
#     plt.scatter(x, y, s=s, alpha = 0.2)

# create_plot(twin_primes, s=5)
# create_plot2(allprimes, s=5)
# plt.show()

def plot_primes_and_twins(allprimes, twin_primes, figsize=8, facecolor = "midnightblue"):
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.axis("off")

    # All primes
    allprimes = np.array(allprimes)
    x1, y1 = get_coordinate(allprimes, 2)

    ax.scatter(
        x1,
        y1,
        s=5,
        alpha=0.2,
        color="#DE7691",
        label="Primes"
    )

    # Twin primes
    twin_primes = np.array(twin_primes)
    twin_nums = twin_primes.T[0] + 1

    x2, y2 = get_coordinate_new(twin_nums, 2)
    x2 = np.array(x2).flatten()
    y2 = np.array(y2).flatten()

    ax.scatter(
        x2,
        y2,
        s=20,
        color="#DE7691",
        label="Twin Primes"
    )

    ax.legend()
    plt.show()


# Usage
plot_primes_and_twins(allprimes, twin_primes)