# Safely iterates over a dictionary copy to modify it during iteration

my_dict = {"temp_a": 1, "perm_b": 2, "temp_c": 3}

for key in list(my_dict.keys()):
    if key.startswith("temp"):
        del my_dict[key]

print(my_dict)  # {'perm_b': 2}
