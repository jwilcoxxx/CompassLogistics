import random
import matplotlib.pyplot as plt
import numpy as np

def generate_random_number():
    return random.gauss(0, 1)

def add_three_numbers():
    return generate_random_number() + generate_random_number() + generate_random_number()

def plot_distribution(data, title):
    plt.hist(data, bins=100, edgecolor='black', alpha=0.7)
    plt.title(title)

num_samples = 100000
random_number_1 = [generate_random_number() for i in range(num_samples)]
random_number_2 = [generate_random_number() for i in range(num_samples)]
random_number_3 = [generate_random_number() for i in range(num_samples)]
sum_of_three = [random_number_1[i] + random_number_2[i] + random_number_3[i] for i in range(num_samples)]

fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(random_number_1, bins=100, edgecolor='black', alpha=0.7)
axs[0, 0].set_title("Distribution of Random Number 1")
axs[0, 1].hist(random_number_2, bins=100, edgecolor='black', alpha=0.7)
axs[0, 1].set_title("Distribution of Random Number 2")
axs[1, 0].hist(random_number_3, bins=100, edgecolor='black', alpha=0.7)
axs[1, 0].set_title("Distribution of Random Number 3")
axs[1, 1].hist(sum_of_three, bins=100, edgecolor='black', alpha=0.7)
axs[1, 1].set_title("Distribution of Sum of Three Numbers")

plt.tight_layout()
plt.show()

