# 0x02-minimum_operations

## Description
This project involves solving a problem where you are given a text file that contains a single character `H`. The text editor you are using can perform only two operations: "Copy All" and "Paste". Your task is to write a function that calculates the minimum number of operations required to end up with exactly `n` characters of `H` in the file.

## Requirements
- Prototype: `def minOperations(n)`
- The function should return an integer representing the minimum number of operations needed.
- If `n` is impossible to achieve, the function should return `0`.

## Example
```python
n = 9
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6
