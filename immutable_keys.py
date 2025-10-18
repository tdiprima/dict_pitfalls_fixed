# Demonstrates that dictionary keys must be immutable, using a tuple instead of a list

my_dict = {(1, 2): "greeting"}
print(my_dict[(1, 2)])  # Outputs: greeting
