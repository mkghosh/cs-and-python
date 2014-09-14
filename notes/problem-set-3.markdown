# Problem set 3

<br>

## Q1 - RADIATION EXPOSURE

一个不稳定的原子损失能量放射带电离子的过程称为 __放射性衰变 (Radioactive decay)__,
即通常所称的辐射 (Radiation).

在 Q1 中, 我们的问题是使用近似算法求一段时间内的辐射总量.

比如说统计一个样品从初始状态开始第 5 年 (结束) 至 第 11 年 (结束) 的放射总量.
可以将该段时间的放射性衰变曲线六等分为六个矩形, 即每个矩形代表一年, 求得所有矩形面积即为粗略估计值.

完成下面的函数:

```python
def f(x):
    import math
    return 10 * math.e**(math.log(0.5) / 5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times.
    Calls the function f to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
    the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
    between start and stop times.
    '''
```

> 注: 这里要注意的是由于时间单位的不同, 有可能遍历一段时间的步长是浮点数.

<br>

## Q2 - A WORDGAME: HANGMAN

如果对于这个游戏的规则不了解, 参考 [wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

要求:

1. 计算机必须从可用单词列表 `words.txt` 中随机挑选一个字母.
2. 该游戏必须是交互式的, 游戏流程如下:
  - 当游戏开始, 输出让玩家知道电脑的可用单词数.
  - 提示玩家每回合输入一个答案.
  - 玩家输入后立刻得到反馈, 该答案是否存在与电脑随机挑选的单词中.
  - 每一轮结束后, 输出用户已经尝试过的部分和剩余可选单词.
3. 一些附加规则:
  - 玩家允许猜 8 次, 每轮要提示玩家剩余尝试次数.
  - 只有当玩家猜错时才损失一次机会.
  - 当玩家重复输入一个字符两次, 提示该字符已经输入过了要重新输入, 且不丢失机会.
  - 整个游戏当玩家猜中全部单词或用完尝试次数后结束, 并显示答案.

Sample Output:

```
Loading word list from file...
55900 words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is 4 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guesss a letter: <user input a>
Good guess: _ a _ _
-------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: <user input a>
Oops! You've already guessed that letter: _ a _ _
-------------
You have 8 guesses left.
......
...... <user input s>
Oops! That letter is not in my word: _ a _ _
-------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
......
......
......
Good guess: tact
-------------
Congratulations, you won!

or

......
Oops! That letter is not in my word e _ _ e
------------
Sorry, you ran out of guesses. The word was else.
```

### PART 1 : Scaffold functions

- 实现函数 `isWordGuessed` 接受两个参数,
字符串 `secretWord` 和字母列表 `lettersGuessed`.
该函数返回一个布尔值: 如果 `secretWord` 的全部单词都在字母列表内为真, 否则为假.
- 实现函数 `getGuessedWord` 接受两个参数,
字符串 `secretWord`, 字母列表 `lettersGuessed`.
该函数返回一个由字母和下划线组成的字符串,
`secretWord` 中的字母存在于字母列表则显示为字母, 否则显示为下划线.
- 实现函数 `getAvailableLetters`, 接受一个字母列表参数 `lettersGuessed`.
该函数返回一个由英文字母 [a-z] 组成的字符串, 在 `lettersGuessed` 中出现的字符__不包含__在内.

> 在 `getAvailableLetters` 中, 因为字符串是不可变对象,
> 移除字符串中的字符可以参考使用 `string.replace(old, new)` 方法.


### PART 2 : Function hangman

有了 part 1 中的功能函数, 现在要实现 `hangman` 函数完成整个游戏流程.
该函数接受一个字符串参数 `secretWord` 即用户输入.

在实现该函数时需要注意以下几点:

1. 确保用户输入为小写 `string.lower()`
2. 注意如何正确使用以下几个信息:
  - 用户输入的猜测
  - 用户目前已经猜过的字符
  - 尝试次数
  - 可用字符列表


参考代码 [hangman.py](https://github.com/HexTeto/cs-and-python/blob/master/src/hangman.py)
