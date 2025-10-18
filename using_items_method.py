# Shows the benefit of using .items() for iterating over keys and values

my_dict = {"animal": "Bear", "color": "Brown"}

# Less efficient
for key in my_dict:
    value = my_dict[key]
    print(key, value)

# More efficient
for key, value in my_dict.items():
    print(key, value)
