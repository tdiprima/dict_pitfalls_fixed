# Bonus trick: Uses set arithmetic on dict keys to check if required keys are present

required = set(["A", "B", "X"])

d1 = {"A": 1, "B": 2, "C": 3}
d2 = {**d1, "X": 4}

print("d1 has all required:", d1.keys() >= required)  # False
print("d2 has all required:", d2.keys() >= required)  # True

# Alternative without set arithmetic
print(all(k in d1 for k in required))  # False
