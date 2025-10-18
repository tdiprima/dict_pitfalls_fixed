## Immutable Vibes

So basically — in Python, **dictionary keys gotta be immutable** (aka unchangeable). That's because Python needs to keep track of keys using their hash values — and if a key could change (like a list), its hash would change too, and Python would lose it in the dictionary like *poof* 🫠

```python
my_dict = {(1, 2): "greeting"}
print(my_dict[(1, 2)])  # Outputs: greeting
```

Using a **tuple `(1, 2)`** as the key, which is valid since tuples are **immutable** — you can't modify their contents after creation.

If you tried using a list instead, like `[1, 2]`, Python would throw a `TypeError` because lists are **mutable**, meaning their contents can change, which makes them unhashable.

So TL;DR:  
✅ Tuples work as dict keys (immutable gang 💪)  
❌ Lists don't (too unstable 😭)
