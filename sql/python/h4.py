web_dev = ["John", "Meera", "Kiran"]
data_science = ["Arjun", "Sneha", "Vikram"]
ui_ux = ["Diya", "Ravi", "Tara"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("Naveen")

data_science.insert(1, "Anjali")

ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

first_two_web = web_dev[:2]
print("First two Web Dev participants:", first_two_web)

name_lengths = [len(name) for name in data_science_copy]
print("Length of each name in copied Data Science list:", name_lengths)

asha_present = "Asha" in web_dev or "Asha" in data_science_copy or "Asha" in ui_ux
print("Is Asha present?", asha_present)

first_participants = (web_dev[0], data_science_copy[0], ui_ux[0])
print("Tuple of first participants:", first_participants)