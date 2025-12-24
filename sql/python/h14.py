import random
import math

names_input = input("Enter customer names (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]

unique_names = list(set(names_list))

random.shuffle(unique_names)

winners = random.sample(unique_names, 2)

reversed_winners = [winner[::-1] for winner in winners]

print("Winner 1:", reversed_winners[0])
print("Winner 2:", reversed_winners[1])

total_participants = len(unique_names)
print("Total unique participants:", total_participants)

sqrt_participants = round(math.sqrt(total_participants))
print("Square root of participants (rounded):", sqrt_participants)