import random
from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np

NUM_TRIALS = 100000

class Person:
    def __init__(self, country):
        self.country = country

totals = {0: 0, 1: 0, 2: 0, 3: 0}
seats = {11: None, 12: None, 13: None, 21: None, 22: None, 23: None}
people = [Person('China'), Person('China'),
          Person('Korea'), Person('Korea'),
          Person('Japan'), Person('Japan')]

for trial_no in range(NUM_TRIALS):

    # make clean copies of initial populations
    people_now = people.copy()
    seats_now = seats.copy()

    # run trial: take seats
    while None in seats_now.values():
        free_seats = [s for s in seats_now if seats_now[s] is None]
        person_to_sit = people_now.pop(random.randint(0, len(people_now) - 1))
        seats_now.update({random.choice(free_seats): person_to_sit})
        
    # check if successful
    reversed_dict = defaultdict(list)
    for seat, person in seats_now.items():
        reversed_dict[person.country].append(seat)
    
    num_adj_pairs = len([pair for pair in reversed_dict.values() if (max(pair) - min(pair)) in {1, 10}])
    totals[num_adj_pairs] += 1
    

simulated_p = [v / NUM_TRIALS for v in totals.values()]
theoretical_p = [2/15, 8/15, 2/15, 1/5]

print(f'Simulation: \t {simulated_p}')
print(f'Theoretical: \t {theoretical_p}')

plt.style.use(r'C:\Users\lnick\Documents\Personal\Programming\Python\Resources\proplot_style_web.mplstyle')

labels = ['0', '1', '2', '3']
label_x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(label_x - width/2, simulated_p, width, label='Simulation')
rects2 = ax.bar(label_x + width/2, theoretical_p, width, label='Theoretical')

ax.set_xlabel('Number of student pairs from same country sitting next to each other')
ax.set_ylabel('Probability mass function (pmf)')
ax.set_xticks(label_x, labels)
ax.legend()
plt.show()