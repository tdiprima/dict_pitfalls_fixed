# Compares manual key checking with using defaultdict for cleaner code

# Manual way
my_dict = {}
key = "language"
if key in my_dict:
    my_dict[key] += 1
else:
    my_dict[key] = 1

# Better way
from collections import defaultdict
count = defaultdict(int)
count["script"] += 1
print(count["script"])  # 1
