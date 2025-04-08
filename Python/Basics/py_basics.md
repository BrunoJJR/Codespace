# Python Basics

---
- [Data Types](#datatypes)
- [Syntax](#syntax)
- [Functions](#functions)
---

## Data Types

### Numeric 
- **Integer (`int`)** → whole numbers, no decimals.
```python
age = 20
```

- **Floating Point (`float`)** → numbers with decimal values.
```python 
height = 182.5
```

- **Complex (`complex`)** → complex numbers with a real and imaginary part.
```python
k = 1j
z = 3 + 5j
#j is the imaginary denotation
```



### Text 
- **String (`str`)** → a sequence of characters.
```python 
name = "Hubert"
```

### Boolean 
- **Boolean (`bool`)** → represents True or False
```python 
alive = True
married = False
```

### Sequences
- **List (`list`)** → ordered and mutable collection of indexable values that allows duplicates:
```python
empty = []
spells = ["Fireball", "Frostbolt", "Arcane Missiles"]
stuff = stuff = [42, "Mage", True, 3.14] # can have multiple types
```

- **Tuple (`tuple`)** → ordered and unmutable collection of indexable values that allows duplicates:
```python
empty = ()
one = (42,)           # must include the comma!
pair = (1, 2)
triple = (1, 2, 3)
lots = ("a", "b", "c", 1, 2, True) # can have multiple types
```
- **Range (`range`)** → a built-in Python type used to generate sequences of numbers, especially useful for loops.
```python
range(start, stop, step) 
# start (optional): where the sequence begins (default is 0)
# stop: where the sequence ends (exclusive: does not include the stop value itself)
# step (optional): the difference between each number (default is 1)
```
Examples:
```python
range(5)           # 0, 1, 2, 3, 4
range(2, 6)        # 2, 3, 4, 5
range(1, 10, 2)    # 1, 3, 5, 7, 9
range(10, 0, -2)   # 10, 8, 6, 4, 2
```
Usage in Loops:
```python
for i in range(5):
    print(i)

# output:
# 0
# 1
# 2
# 3
# 4
```
### Mapping
- **Dictionary (`dict`)** → key-value pairs, unordered and mutable.
```python
character = {"name": "Pyroblastio", "class": "Mage", "level": 60}
```

### Set
- **Set (`set`)** → unordered and mutable collection of unindexable values that does NOT allow duplicates.
```python
buffs = {"Arcane Intellect", "Stamina", "Arcane Intellect"}
```

- **Frozen Set (`frozenset`)** → exactly like a set, but immutable.
```python
elements = frozenset(["fire", "water", "air"])
```

### Binary

- **Bytes(`bytes`)** →

- **Byte Array(`bytearray)** →

- **Memory View (`memoryview`)** →


## None/Null

- **None Type (`NoneType`)** →






---

## Syntax
- `#` is used to comment a single line in Python.
For multi-line comments, you usually just use multiple single-line comments:

```python
# Line 1
# Line 2
# Line 3
```
- By convention, Python follows snake case.
```python 
a_variable_name = "name"
```
- Variables are case sensitive.
```python
a = 3
A = False
#A will not overwrite a, they are two different variables
```
- Python allows you to assign values to multiple variables in one line:
```python
x, y, z = "Orange", "Banana", "Cherry"
```
- And you can assign the same value to multiple variables in one line:
```python
x = y = z = "Orange"
```

- Variables that are created outside of a function are known as global variables. They can be used by everyone, both inside of functions and outside.
```python
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword:
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

Also, to change the value of a global variable inside a function, refer to the variable by using the global keyword:
```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

---


#### Functions
- **`print()`** → can be used to display output on the terminal/console.
```python
print("Hello World!")
```
In the print() function, you can output multiple variables, separated by a comma:
```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

- **`type()`** → used to determine the type of something.
```python
x = 5
print(type(x))
```




