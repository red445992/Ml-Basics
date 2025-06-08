# Python Built-in Data Structure Methods

A quick reference for commonly used methods on Python's built-in data structures: **List**, **Dictionary**, **Set**, and **Tuple**.

---

## 📋 List Methods

| Method      | Description                                                        |
|-------------|--------------------------------------------------------------------|
| append()    | Adds an element at the end of the list                             |
| clear()     | Removes all the elements from the list                             |
| copy()      | Returns a copy of the list                                         |
| count()     | Returns the number of elements with the specified value            |
| extend()    | Adds the elements of an iterable to the end of the list            |
| index()     | Returns the index of the first element with the specified value    |
| insert()    | Adds an element at the specified position                          |
| pop()       | Removes the element at the specified position                      |
| remove()    | Removes the item with the specified value                          |
| reverse()   | Reverses the order of the list                                     |
| sort()      | Sorts the list                                                     |

**List Comprehension Example:**  
```python
newlist = [expression for item in iterable if condition]
```

---

## 📖 Dictionary Methods

| Method        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| clear()       | Removes all the elements from the dictionary                                |
| copy()        | Returns a copy of the dictionary                                            |
| fromkeys()    | Returns a dictionary with the specified keys and value                      |
| get()         | Returns the value of the specified key                                      |
| items()       | Returns a list containing a tuple for each key-value pair                   |
| keys()        | Returns a list containing the dictionary's keys                             |
| pop()         | Removes the element with the specified key                                  |
| popitem()     | Removes the last inserted key-value pair                                    |
| setdefault()  | Returns the value of the specified key. If not found, inserts the key/value |
| update()      | Updates the dictionary with the specified key-value pairs                   |
| values()      | Returns a list of all the values in the dictionary                          |

---

## 🟢 Set Methods

| Method                     | Shortcut | Description                                                                 |
|----------------------------|----------|-----------------------------------------------------------------------------|
| add()                      |          | Adds an element to the set                                                  |
| clear()                    |          | Removes all the elements from the set                                       |
| copy()                     |          | Returns a copy of the set                                                   |
| difference()               | -        | Returns a set containing the difference between two or more sets            |
| difference_update()        | -=       | Removes the items in this set that are also included in another set         |
| discard()                  |          | Removes the specified item                                                  |
| intersection()             | &        | Returns a set, that is the intersection of two other sets                   |
| intersection_update()      | &=       | Removes the items in this set that are not present in other set(s)          |
| isdisjoint()               |          | Returns whether two sets have an intersection or not                        |
| issubset()                 | <=, <    | Returns whether another set contains this set or not                        |
| issuperset()               | >=, >    | Returns whether this set contains another set or not                        |
| pop()                      |          | Removes an element from the set                                             |
| remove()                   |          | Removes the specified element                                               |
| symmetric_difference()     | ^        | Returns a set with the symmetric differences of two sets                    |
| symmetric_difference_update() | ^=    | Inserts the symmetric differences from this set and another                 |
| union()                    | &#124;   | Returns a set containing the union of sets                                  |
| update()                   | &#124;=  | Updates the set with the union of this set and others                       |

---

## 🟣 Tuple Methods

| Method   | Description                                                        |
|----------|--------------------------------------------------------------------|
| count()  | Returns the number of times a specified value occurs in a tuple    |
| index()  | Searches the tuple for a specified value and returns its position  |

---

> _This document is a handy reference for Python beginners and those revising core data structure operations._