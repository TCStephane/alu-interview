# Rain

Given a list of non-negative integers representing the heights of walls with
unit width 1, calculate how many square units of water are retained after it
rains.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- PEP 8 style (1.7.x)
- No module imports allowed
- All files are executable and start with `#!/usr/bin/python3`

## Files

| File | Description |
| --- | --- |
| `0-rain.py` | Defines `rain(walls)`, returning the total water retained |

## Usage

```
$ cat 0_main.py
#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

$ ./0_main.py
6
6
```

## Approach

Two pointers move inward from both ends of the list, tracking the highest wall
seen from each side. The shorter side is always processed, since its water
level is bounded by its own max. This runs in O(n) time and O(1) space.
