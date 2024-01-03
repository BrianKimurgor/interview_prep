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
```

- __balance__ is the array name
- __array.array__ is the module
- __'i'__ is the data type
- the values in brackets are the elements

## Accessing specific array values
###Syntax
```python
arrayName[indexNum]
```

##Array operations
### Insert
With this operation, you can insert one or more items into an array at the beginning,
end,or any given index of the array
- This method expects an index and a values
###Syntax
```python
arrayName.insert(index, value)
```
- This adds a new value to an array

###Delete
You can delete one item from an array by value
- This method accepts only one argument, the value
###Syntax
```python
arrayName.remove(value)
```

###searching
With this operation, you can search for an item in an array based on its value.
- This method accepts only one argument, the value, it does not affect array values
###Syntax
```python
arrayName.index(values)
```
###Update
This operation replaces the existing value at the given index
thus assigning a new value at the given index
- This method accepts two values, index and value
###Syntax
```python
arrayName.update(index, value)
```
###Traverse
you can traverse a python array using loops
```python
import array
balance = array.array('i', [3, 200, 340])
for x in balance:
    print (x)
    ```
###Output
```python
3
200
340
```
##Big O
# Time Complexity of Array Operations

| Operation              | Big-O       | Note                                                                                           |
|------------------------|-------------|------------------------------------------------------------------------------------------------|
| Access                 | O(1)        | Constant time complexity for accessing an element by its index.                                |
| Search                 | O(n)        | Linear time complexity for searching an element in an unsorted array.                           |
| Search (sorted array)  | O(log(n))   | Logarithmic time complexity for searching an element in a sorted array using binary search.      |
| Insert                 | O(n)        | Linear time complexity. Insertion requires shifting all subsequent elements to the right.        |
| Insert (at the end)    | O(1)        | Constant time complexity for inserting an element at the end when no shifting is required.       |
| Remove                 | O(n)        | Linear time complexity. Removal requires shifting all subsequent elements to the left.            |
| Remove (at the end)    | O(1)        | Constant time complexity for removing the last element when no shifting is required.             |
