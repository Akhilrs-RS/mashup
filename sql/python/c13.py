item = input("Enter the name of the new item: ")

file_name = "items.txt"

try:
    with open(file_name, "a") as file:
        file.write(item + "\n")
except FileNotFoundError:
    with open(file_name, "w") as file:
        file.write(item + "\n")

print("\nCurrent list of items:")

with open(file_name, "r") as file:
    for line in file:
        print(line.strip())