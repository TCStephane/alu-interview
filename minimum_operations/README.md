# Minimum Operations

Calculates the fewest number of operations (`Copy All` and `Paste`) needed
to get exactly `n` `H` characters in a file that starts with a single `H`.

## Usage
```
$ ./0-main.py
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```

## Files
- `0-minoperations.py`: `minOperations(n)` returns the minimum number of
  operations, or `0` if `n` is impossible to achieve.
- `0-main.py`: example usage.

## How it works
The answer is the sum of the prime factors of `n`.
