# Python Basics

---

## Table of Contents
- [Data Types](#data-types)
- [Syntax](#syntax)
- [Functions](#functions)

---

## Data Types

### Numeric 

- **Integer (`int`)** → Represents whole numbers without a fractional part.
Used in counting, indexing, loop counters, etc.
```python
age = 30
year = 2024
score = -5
```

- **Floating Point (`float`)** → Represents numbers with decimal points.
Used for measurements, percentages, financial data, etc.
```python 
height = 1.82
price = 99.99
temperature = -4.5
```

- **Complex (`complex`)** → Numbers with real and imaginary parts.
Useful in scientific and engineering calculations.
```python
z = 3 + 5j
print(z.real)   # 3.0
print(z.imag)   # 5.0
```

---

### Text 

- **String (`str`)** → A sequence of characters used to store text.
Used for messages, names, descriptions, etc.
```python 
name = "Hubert"
greeting = "Hello, " + name
print(greeting)  # Hello, Hubert
```

You can also use:
```python
multiline = """This is
a multiline
string."""
```

---

### Boolean 

- **Boolean (`bool`)** → Logical values representing truth.
Used in conditions, comparisons, control flow.
```python 
is_alive = True
is_admin = False
print(5 > 2)  # True
print(3 == 4)  # False
```

---

### Sequences

- **List (`list`)** → Ordered, mutable and indexable collection of items that allows duplicates.
Used when you need an editable sequence of values.
```python
items = ["sword", "shield", "potion"]
items.append("bow")
items[0] = "magic sword"
```

- **Tuple (`tuple`)** → Ordered, immutable and indexable collection of items that allows duplicates.
Used for fixed collections, such as coordinates or RGB values.
```python
position = (100, 200)
rgb = (255, 100, 75)
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

---

### Mapping

- **Dictionary (`dict`)** → Unordered, mutable and unindexable collection of key-value pairs.
Used for fast lookups, configs, JSON-like structures.
```python
user = {"charname": "Maguskin", "level": 60}
user["class"] = "Mage"
print(user["level"])
```

---

### Set

- **Set (`set`)** → Unordered, mutable and unindexable collection of unique elements.
Used to remove duplicates, fast membership testing, math set operations.
```python
buffs = {"Stamina", "Arcane Intellect"}
buffs.add("Spirit")
print("Spirit" in buffs)
```

- **Frozen Set (`frozenset`)** → Like a set, but immutable.
Used when you need a constant collection for hashing or as a dictionary key.
```python
elements = frozenset(["fire", "water", "air"])
```

---

### Binary

- **Bytes (`bytes`)** → Immutable sequence of raw bytes (0–255).
Used for binary files, network protocols, low-level data.
```python
data = b"hello"
print(data[0])  # 104
```

- **Byte Array (`bytearray`)** → Mutable version of `bytes`.
Used when you need to edit binary data.
```python
buffer = bytearray(b"hello")
buffer[0] = 72
print(buffer)  # bytearray(b'Hello')
```

- **Memory View (`memoryview`)** → Efficient view over binary data, no copy.
Used for working with large data buffers.
```python
mv = memoryview(b"world")
print(mv[1])  # 111 (ASCII for 'o')
```

---

### None / Null

- **None Type (`NoneType`)** → Represents the absence of a value.
Common in default arguments, null checks, and uninitialized variables.
```python
result = None

if result is None:
    print("No result yet.")
```

---

## Syntax

- **Comments** → Used to describe code or temporarily disable lines.
`#` is used to comment a single line in Python.
```python
# Explaining what the following line does:
x = 5
```
For multi-line comments, you usually just use multiple single-line comments:
```python
# Line 1
# Line 2
# Line 3
```

- **Snake Case** → Naming convention using underscores.
```python
user_name = "User's name"
```

- **Case Sensitivity** → Python differentiates variable names by case.
```python
a = 10
A = 20
# A will not overwrite a, they are two different variables
```

- **Multiple Assignment** → Python allows you to assign values to multiple variables in one line.
```python
x, y, z = "Orange", "Banana", "Cherry"
```
And you can assign the same value to multiple variables in one line:
```python
a = b = c = "Orange"
```

- **Global vs Local Variables** → Variables that are created outside of a function are known as global variables. They can be used by everyone, both inside of functions and outside.
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

- **Global Keyword (`global`)** → Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword:
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

## Unpacking

Unpacking allows you to assign elements from a collection (like a list or tuple) directly into individual variables in a single line.
It makes code cleaner and easier to read and is useful when you know the exact number of elements.

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)  # apple
print(y)  # banana
print(z)  # cherry
```

You can also use `*` to unpack the remaining values:

```python
numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers
print(a, b)     # 1 2
print(rest)     # [3, 4, 5]
```

---

## Functions

Functions are reusable blocks of code that perform specific tasks.

The `print()` function displays output to the terminal or console.

```python
print("Welcome to Python!")
```

Print multiple values:
```python
name = "Hubert"
print("Hello", name, "!")  # Hello Hubert !
```

---

Use `type()` to check the data type of any value.

```python
print(type(42))       # <class 'int'>
print(type("Hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
```

---

### Custom Functions

You can define your own functions using the `def` keyword.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Hubert"))  # Hello, Hubert!
```

- `name` is a parameter (input to the function)
- `return` gives back a result

---

#### Functions with Default Arguments

Default arguments provide fallback values when no input is given.

```python
def say_hello(name="friend"):
    print(f"Hello, {name}!")

say_hello()           # Hello, friend!
say_hello("Hubert")   # Hello, Hubert!
```

---

### Returning Values

Functions can return data using the `return` keyword.

```python
def square(x):
    return x * x

result = square(5)
print(result)  # 25
```

You can return any type: numbers, strings, lists, etc.
