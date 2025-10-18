# Uses OrderedDict to guarantee insertion order across Python versions

from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

for key in od:
    print(key)  # Outputs: first, second, third in order
