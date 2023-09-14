#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0        
    weight_sum = 0
    total = 0
    for score, weight in my_list:
        weight_sum += score * weight
        total += weight
    return (weight_sum / total)
