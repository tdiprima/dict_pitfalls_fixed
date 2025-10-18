# Compares inefficient and efficient ways to check for key existence

my_dict = {"title": "Book"}

# Inefficient
if "title" in list(my_dict.keys()):
    print("Found")

# Efficient
if "title" in my_dict:
    print("Found")
