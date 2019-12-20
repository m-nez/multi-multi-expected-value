import numpy as np
from numpy import nan
from scipy.special import comb
import matplotlib.pyplot as plt

reward = [
[250_000,nan,nan,nan,nan,nan,nan,nan,nan,nan],
[10_000,70_000,nan,nan,nan,nan,nan,nan,nan,nan],
[520,2_000,22_000,nan,nan,nan,nan,nan,nan,nan],
[140,300,600,6_000,nan,nan,nan,nan,nan,nan],
[12,42,60,200,1_300,nan,nan,nan,nan,nan],
[4,8,20,20,120,700,nan,nan,nan,nan],
[2,2,4,4,8,20,84,nan,nan,nan],
[0,0,0,2,2,4,8,54,nan,nan],
[0,0,0,0,0,0,2,2,16,nan],
[0,0,0,0,0,0,0,0,0,4]
]

num_total = 80
num_winning = 20
num_losing = num_total - num_winning

expected_rewards = []
num_typed_range = range(1, 11)

for num_typed in num_typed_range:
    total_combinations = comb(num_total, num_typed, exact=True)
    reward_times_winning_combinations = 0
    for num_hit in range(1, num_typed + 1):
        r = reward[-num_hit][-num_typed]
        winning_combinations = comb(num_winning, num_hit, exact=True) \
                * comb(num_losing, num_typed - num_hit, exact=True)

        reward_times_winning_combinations += r * winning_combinations

    expected_reward = reward_times_winning_combinations / total_combinations
    print("expeced_reward(num_typed={}) =".format(num_typed), expected_reward)
    expected_rewards.append(expected_reward)

plt.bar(num_typed_range, expected_rewards)
plt.ylabel("Wartość oczekiwana wygranej [PLN]")
plt.xlabel("Ilość typowanych liczb")
plt.ylim([0.95, 1.03])
plt.xticks(num_typed_range, num_typed_range)
plt.show()
