import random
import numpy as np
from matplotlib import pyplot as plt
from time import perf_counter
import pandas as pd

r_time = [None] * 1000
for el in range(len(r_time)):
    i = 0
    tic = perf_counter()
    while i <= el:
        random.random()
        i += 1
    tac = perf_counter()
    r_time[el] = tac - tic

r_np_time = [None] * 1000

for el in range(len(r_np_time)):
    tic = perf_counter()
    np.random.random(el)
    tac = perf_counter()
    r_np_time[el] = tac - tic

std_lib = list(zip(range(1, 1001), r_time, ['standard'] * 1000))
d_r = pd.DataFrame(std_lib, columns=['freq', 'time_to_complete', 'library'])

np_lib = list(zip(range(1, 1001), r_np_time, ['numpy'] * 1000))

d_np = pd.DataFrame(np_lib, columns=['freq', 'time_to_complete', 'library'])

d_draw = pd.merge(d_r, d_np, how='outer')

groups = d_draw.groupby('library')
fig, ax = plt.subplots()
for name, group in groups:
    ax.plot(group.freq, group.time_to_complete, label=name)
ax.legend()
ax.set_title('Comparing different random functions from numpy and standard random')
ax.set_xlabel('Length of sequence')
ax.set_ylabel('Time to complete')
plt.show()


# crate and visualise distribution in time of monkey sorting
def is_sorted(l_t_check):
    return all(l_t_check[i] <= l_t_check[i + 1] for i in range(len(l_t_check) - 1))


def monkey_sort(to_sort):
    if not is_sorted(to_sort):
        for i in range(len(to_sort)):
            rand_point = random.randint(0, len(to_sort) - 1)
            to_sort[i], to_sort[rand_point] = to_sort[rand_point], to_sort[i]
    else:
        return to_sort


t2_inf = []
for i in range(1000, 11000, 1000):
    for j in range(10):
        test_seq = list(np.random.randint(0, 1000000, i))
        tic = perf_counter()
        monkey_sort(test_seq)
        tac = perf_counter()
        t2_inf.append([i, tac - tic])

t2_draw = pd.DataFrame(t2_inf, columns=['length_of_sequence', 'time_to_complete'])

t2_draw.boxplot(by='length_of_sequence', return_type=None)
plt.suptitle('')
plt.title('Boxplot of distribution in time depending on length of sequence to sort by monkey sort')
plt.xlabel('Length of Sequence')
plt.ylabel('Time to sort')
plt.show()

# random walk visualisation
n_step = 5000
x = [0] * n_step
y = [0] * n_step

steps = ['up', 'down', 'left', 'right']
for i in range(1, n_step):

    step = random.choice(steps)
    if step == "right":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif step == "left":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif step == "up":
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif step == "down":
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1


plt.plot(x, y)
plt.title('Random Walk in 2D')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# change letters in text

test_text = 'Random is not your choice my friend'


def change_letters(input_text):
    split_text = test_text.split()
    result = []
    for word in split_text:
        if len(word) >= 4:
            letters = list(word[1:-1])
            random.shuffle(letters)
            shuffled_letter = [word[0]] + letters + [word[-1]]
            result.append(''.join(shuffled_letter))
        else:
            result.append(word)
    return ' '.join(result)


# print(change_letters(test_text))
