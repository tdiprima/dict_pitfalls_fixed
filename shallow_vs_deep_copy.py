# Highlights the difference between shallow copy and deep copy for nested dictionaries

import copy

a = {"details": {"name": "Bear"}}
b = a.copy()
b["details"]["name"] = "Wolf"
print(a["details"]["name"])  # Wolf

# Deep copy fix
c = copy.deepcopy(a)
c["details"]["name"] = "Fox"
print(a["details"]["name"])  # Wolf (unchanged)
