## `in my_dict` or nah?

In Python, checking if a key exists can be done two ways — but one's kinda goofy 💀

```python
# Inefficient
if "title" in list(my_dict.keys()):
    print("Found")
```

This version literally builds a **whole list** of the dictionary's keys just to check one item. That's extra work for no reason — like converting your playlist to vinyl just to play one song 😭

Then there's the smart way:

```python
# Efficient
if "title" in my_dict:
    print("Found")
```

Here, Python directly checks the dictionary's internal hash table — way faster, no unnecessary conversions. 🚀

So TL;DR:  
✅ `"key" in my_dict` → efficient, clean, pro move  
❌ `"key" in list(my_dict.keys())` → slow, dramatic, not it

<br>
