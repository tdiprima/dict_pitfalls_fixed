## DefaultDict (ADHD friendly)

```py
from collections import defaultdict

data = [('Apple', 10), ('Banana', 5), ('Apple', 15), ('Cherry', 20)]
inventory = defaultdict(int) 
for item, count in data:
    # No need to check if 'item' is already a key!
    inventory[item] += count 
print(dict(inventory))
# Output: {'Apple': 25, 'Banana': 5, 'Cherry': 20}
```

Okay, let's break it down real simple, Bear-style 😎

So normally, when you use a regular dictionary (`dict`), if you try to do something like this:

```python
inventory[item] += count
```

and `item` **doesn't exist yet**, Python freaks out and says `KeyError`.
You'd usually have to do this:

```python
if item in inventory:
    inventory[item] += count
else:
    inventory[item] = count
```

That's kinda annoying to write every time.

### Enter `defaultdict` 🚀

When you create one with:

```python
inventory = defaultdict(int)
```

you're saying:

"Hey Python, if a key doesn't exist yet, automatically create it — and set its value to `int()`."

Now, `int()` by default returns `0`.

So the first time `inventory['Apple']` is accessed, Python's like:

"Oh, that key doesn't exist. Let me make it real quick and set it to 0."

Then it does:

```python
inventory['Apple'] += 10
# which becomes 0 + 10
```

Next time it sees `'Apple'`, the key already exists, so it just adds again.

### What happens step by step 🧠

Your data:

```python
[('Apple', 10), ('Banana', 5), ('Apple', 15), ('Cherry', 20)]
```

Loop:

1. `'Apple'` not in dict → auto-created as 0 → 0 + 10 = 10
2. `'Banana'` not in dict → auto-created as 0 → 0 + 5 = 5
3. `'Apple'` already exists (10) → 10 + 15 = 25
4. `'Cherry'` not in dict → auto-created as 0 → 0 + 20 = 20

Final result:

```python
{'Apple': 25, 'Banana': 5, 'Cherry': 20}
```

### TL;DR 🍎🍌🍒

`defaultdict(int)` = a dictionary that automatically starts every new key at 0.
You can also use other defaults:

* `defaultdict(list)` → starts each new key as `[]`
* `defaultdict(dict)` → starts each new key as `{}`

<br>
