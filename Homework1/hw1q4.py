#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
"""

@author: slefever1

Monte carlo simulation
"""

print('Enter number of dice rolls: ')
n = int(input())

die_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
die_prob_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in range(n):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1+die2
    die_dict[sum] = die_dict[sum] + 1

for die_roll in die_dict:
    die_prob_dict[die_roll] = round((100*(float(die_dict[die_roll]) / float(n))), 2)
    
print('Dice rolls: ', die_dict)
print('Dice roll probabilities: ', die_prob_dict)