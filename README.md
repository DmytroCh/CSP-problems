Constraint satisfaction problems
---
There are solutions for two CSP problems:
- N queens  - `chess.py`
- Number as sum of Fibonacci numbers - `fibonacci.py`

For both problems next algorithms were implemented:

- Backtracking
- Forward checking

you can change next parameters:
1) Algorithm: `method = 'f'  # 'b' - backtraking, 'f' - forwardchecking`
2) Chessboard size (chess.py): `size = 8  # size of chessboard`
3) Value for dividing (fibonacci.py): `value = 64  # number to be divided`

N queens problem
---
N queens problem is the problem of placing N queens on a NxN chessboard such that none of them 
attack one another.

Wiki: https://en.wikipedia.org/wiki/Eight_queens_puzzle

Number as sum of Fibonacci numbers problem:
---
Number as sum of Fibonacci numbers problem is the problem of finding all possible combination 
of Fibonacci numbers which sum equals to given number.

Result example for given value 64:
```[[13, 5, '.', 8, 1, 3, '.', '.', 34],
 ['.', 5, '.', '.', 1, 3, 55, '.', '.'],
 ['.', 5, '.', '.', 1, 3, '.', 21, 34],
 ['.', '.', '.', 8, 1, '.', 55, '.', '.'],
 ['.', '.', '.', 8, 1, '.', '.', 21, 34]]```
