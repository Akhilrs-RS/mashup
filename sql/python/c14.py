import random
import math

names_input = input("Enter guest names (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]

unique_names = list(set(names_list))

selected_name = random.choice(unique_names)

reversed_name = selected_name[::-1]

print("Selected name (reversed):", reversed_name)

total_unique = len(unique_names)
print("Total unique names:", total_unique)

rounded_sqrt = round(math.sqrt(total_unique))
print("Rounded square root of total names:", rounded_sqrt)