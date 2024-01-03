# This is a section of preparation dealing with arrays.

## Introduction
- __Array__ is a data structure for storing more than one data item that has a similar data type.
- Items of an array are allocated adjacent memory locations called __elements__.
- Total number of elements in an array is called __length__.
- __Index__ of an array is it's position.

## Advantages of arrays
- they are best for storing multiple values in a single variable
- better at processing many values easily and quickly
- sorting and searching the values is easier

## Creating an array in python
- module for creating an array is called **array**
- Ensure you import before starting on them
### Creating an array in python
```python
import array
balance = array.array('i', [300, 200, 100])
print (balance)
