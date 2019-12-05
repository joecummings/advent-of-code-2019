import multiprocessing
import time

curr_masses = list()
with open("input.txt") as input_file:
    for line in input_file:
        curr_masses.append(int(line))

def fuel_calc(mass: int) -> int:
    return mass // 3 - 2

def find_sum_parallel(masses: list) -> int:
    with multiprocessing.Pool() as pool:
        return sum(pool.map(fuel_calc, masses))
    
start = time.time()
print(find_sum_parallel(curr_masses))
print(time.time() - start)

def find_sum(masses: list) -> int:
    return sum(mass // 3 - 2 for mass in masses)

start = time.time()
print(find_sum(curr_masses))
print(time.time() - start)
