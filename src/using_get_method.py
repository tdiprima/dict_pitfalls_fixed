# Illustrates the .get() method for safely accessing keys with defaults
# Avoids "KeyError"

data = {"name": "Bear"}
print(data.get("height"))  # None
print(data.get("height", 180))  # 180
