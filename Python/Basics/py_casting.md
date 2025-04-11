# Python Type Casting

---
For a deeper explanation of data types, [check this section in **py_basics.md**](py_basics.md#data-types).


## Table of Contents
- [Type Casting Basics](#What-is-type-casting)
- [Summary Table](#type-casting-summary-table)

### What is type casting?

**Type casting** (also called type conversion) is the process of converting one data type into another. Python gives you built-in functions to do this explicitly (you tell it to) or implicitly (Python does it for you). It can prove especially useful to:

- Avoid type errors when combining data

- Get input from a user (which usually comes in as a string) and converting it to something else;

- Ensure proper math or comparison operations;

- Manipulate data structures;

Additionally there are two major types of casting:

- **Explicit Casting** → You manually convert one type to another using built-in functions.
```python 
age_str = "25"
age_int = int(age_str)
print(age_int + 5)  # 30
```

Or
```python 
score = 90
message = "Your score is " + str(score)
print(message)  # Your score is 90
```


- **Implicit Casting** → Python automatically converts values to the appropriate type when needed.
```python
x = 10       # int
y = 2.5      # float
z = x + y    # Python converts int to float automatically

print(z)     # 12.5 (float)
```

### Type Casting Summary Table 

This is a full overview of Python type casting functions, what they convert **to**, what they can convert **from**, and **example usage** for each.


**`int()`** → Converts to Integer

Converts from: `float`, `str` (numeric), `bool`
```python
int(3.9)        # 3
int("42")       # 42
int(True)       # 1
```

---

**`float()`** → Converts to Float

Converts from: `int`, `str` (numeric), `bool`
```python
float(5)        # 5.0
float("3.14")   # 3.14
float(False)    # 0.0
```

---

**`str()`** → Converts to String

Converts from: Any type
(`int`, `float`, `list`, `bool`, etc.)
```python
str(123)              # "123"
str([1, 2, 3])        # "[1, 2, 3]"
str(True)             # "True"
```

---

**`bool()`** → Converts to Boolean

Converts from: Any type 

Values that evaluate to **`False`** are: 
`0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`
```python
bool(0)         # False
bool("hi")      # True
bool([])        # False
```

---

**`list()`** → Converts to List

Converts from: Iterables
(`str`, `tuple`, `range`, `set`)
```python
list("abc")         # ['a', 'b', 'c']
list((1, 2, 3))      # [1, 2, 3]
list(range(3))       # [0, 1, 2]
```

---

**`tuple()`** → Converts to Tuple

Converts from: Iterables
(`str`, `tuple`, `range`, `set`)
```python
tuple([1, 2])        # (1, 2)
tuple("hi")          # ('h', 'i')
```

---

**`set()`** → Converts to Set

Converts from: Iterables
(`str`, `tuple`, `range`, `set`)
(removes duplicates)
```python
set([1, 2, 2, 3])    # {1, 2, 3}
set("hello")         # {'h', 'e', 'l', 'o'}
```

---

**`frozenset()`** → Converts to Frozen Set

Converts from: Iterables
(`str`, `tuple`, `range`, `set`)
```python
frozenset(["a", "b", "c"])  # frozenset({'a', 'b', 'c'})
```

---

**`dict()`** → Converts to Dictionary

Converts from: Sequence of key-value pairs or keyword arguments
```python
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
dict(x=10, y=20)           # {'x': 10, 'y': 20}
```

---

**`bytes()`** → Converts to Bytes

Converts from: `str` (requires encoding), `list` of integers, `bytearray`
```python
bytes("hello", "utf-8")         # b'hello'
bytes([72, 101, 108])           # b'Hel'
```

---

**`bytearray()`** → Converts to Bytearray

Converts from: Same as **`bytes`**, but result is mutable
```python
bytearray("hi", "utf-8")        # bytearray(b'hi')
```

---

**`memoryview()`** → Create Memory View

Converts from: `bytes` or `bytearray`
```python
memoryview(b"hello")           # <memory at ...>
```




