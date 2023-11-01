import time
from functools import lru_cache
from functools import cache
from cachetools import cached
from cachetools.keys import hashkey

f = open("Day 19 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

lines = fileinput.splitlines()

blueprints = {}

cutoff = 100

for i in lines:
    temp = i.split(" ")

    blueprints[int(temp[1][:-1])] = (int(temp[6]), int(temp[12]), int(temp[18]), int(temp[21]), int(temp[27]), int(temp[30]))  

@lru_cache(maxsize=5000000)
def get_maximum(ore, c, ob, g, orer, cr, obr, gr, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten):


    time -= 1


    if time == -1:
        return max(max_gotten, g)


    max_possible = (time * (time - 1)) // 2 + g + (gr * (time + 1))

    if max_possible + 1<= max_gotten:
        return max_gotten

    if ore >= orer_cost:
        produce_ore_robot = True
    else:
        produce_ore_robot = False
    if ore >= clayr_cost:
        produce_clay_robot = True
    else:
        produce_clay_robot = False
    if ore >= obr_cost_in_ore and c >= obr_cost_in_clay:
        produce_ob_robot = True
    else:
        produce_ob_robot = False
    if ore >= gr_cost_in_ore and ob >= gr_cost_in_ob:
        produce_geo_robot = True
    else:
        produce_geo_robot = False

    


    ore += orer
    c += cr
    ob += obr
    g += gr


    
    max_gotten = max(g, max_gotten)

    

    if produce_geo_robot:
        max_gotten = max(max_gotten, get_maximum(ore-gr_cost_in_ore, c, ob-gr_cost_in_ob, g, orer, cr, obr, gr+1, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten))
    if produce_ob_robot and obr < gr_cost_in_ob:
        max_gotten = max(max_gotten, get_maximum(ore-obr_cost_in_ore, c-obr_cost_in_clay, ob, g, orer, cr, obr+1, gr, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten))
    if produce_ore_robot and orer < max(orer_cost, clayr_cost):
        max_gotten = max(max_gotten, get_maximum(ore-orer_cost, c, ob, g, orer+1, cr, obr, gr, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten))
    if produce_clay_robot and cr < obr_cost_in_clay:
        max_gotten = max(max_gotten, get_maximum(ore-clayr_cost, c, ob, g, orer, cr+1, obr, gr, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten))

    if not (produce_ore_robot and produce_clay_robot and produce_ob_robot and produce_geo_robot):
        max_gotten = max(max_gotten, get_maximum(ore, c, ob, g, orer, cr, obr, gr, orer_cost, clayr_cost, obr_cost_in_ore, obr_cost_in_clay, gr_cost_in_ore, gr_cost_in_ob, time, max_gotten))



    return max_gotten

total = 0
final = {}

for i in blueprints:
    v = blueprints[i] #v for values of the costs of each robot
    t1 = time.time()
    result = get_maximum(0, 0, 0, 0, 1, 0, 0, 0, v[0], v[1], v[2], v[3], v[4], v[5], 24, 0)
    final[i] = result
    total += result * i
    t2 = time.time()

print(total)


#Day 2



total = 1

for i in range(1, 4):
    v = blueprints[i]
    t1 = time.time()
    result = get_maximum(0, 0, 0, 0, 1, 0, 0, 0, v[0], v[1], v[2], v[3], v[4], v[5], 32, 0)
    total *= result

print(total)


