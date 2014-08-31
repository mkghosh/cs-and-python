# Week 2 - Simple Algorithms

<br>

### Successive Approximation

Suppose we now want to find the square root of any non-negative number

- Can't guarantee exact answer, but just look for something close enough.
- Start with exhaustive enumeration.
  + take small steps to generate guesses in order.
  + check to see if close enough.

Example code:

```python
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
res = 0.0

while (abs(res**2 - x)) >= epsilon and res <= x:
    res += step
    numGuesses += 1
print('numGuess =', numGuesses)
if abs(res**2 - x) >= epsilon:
    print('Failed on square root of' + str(x))
else:
    print(str(res) + ' is close to the square root of ' + str(x))
```

Some observations

- Step could be any small number
  + if too small, takes a long time to find square root
  + if make too large, might skip over answer without getting close enough

<br>

### Bisection Search

Let's go back to the idea of trying to find the square root.
We know that the square root of `x` lies somewhere between `0` and `x`
from mathematics,
so rather than exhaustive enumeration, suppose instead we pick a number `g`
in the middle of this range, and then:

1. If not close enough, is guess too big or too small?
2. If `g**2 > x`, then we know `g` is too big and we know that the square root
has to lie somewhere between `0` and `g`;
Similarly, if `g**2 < x`, that says `g` is too small,
and we know that the actual value has to lie somewhere between `g` to `x`.
3. Update the variable `g` in the middle of new range.
4. Repeat above processes.

<br>

### Newton - Raphson Root Finding

General approximation algorithm to find roots of a polynomial
in on variable.

[see more...](http://baike.baidu.com/view/643093.htm?fr=aladdin#7)
