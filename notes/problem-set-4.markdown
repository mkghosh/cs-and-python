# Problem set 4

在 P4 我们将实现两个版本的 "the 6.00 word game".

简述其规则如下:

```
Dealing

    1. A player is dealt a hand of `n` letters chosen at random (assume `n=7` for now).
    2. The player arranges the hand into as many words as they want out of the letters,
       using each letter at most once.
    3. some letters may remain unused (these won't be scored).


Scoring

    1. The score for the hand is the sum of the scores for each word formed.
    2. The score for a word is the sum of the points for letters in the word,
       multiplied by the length of the word, plus 50 points if all n letters
       are used on the first word created.
    3. Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3,
       D is worth 2, E is worth 1, and so on. We have defined the dictionary
       SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble
       letter value.
    4. For example, 'weed' would be worth 32 points ((4+1+1+2) for the four lettes,
       then multiply by len('weed') to get (4+1+1+2)*4=32). Be sure to check that
       the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
    5. As another example, if n=7 and you make the word 'waybill' on the first try,
       it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105,
       plus and additional 50 point bonus for using all n letters).
```

参考代码实现 [part 1](https://github.com/HexTeto/cs-and-python/blob/master/src/wordGame/ps4a.py),
[part 2](https://github.com/HexTeto/cs-and-python/blob/master/src/wordGame/ps4b.py)

### P1 - Word Scores

实现 `getWordScore` 计算一个单词的得分数, 该函数接收小写字母组成的字符串, 返回该字符串的得分数.
该函数需要用到的全局常量已经定义在代码框架中.

### P2 - Dealing with Hands

"HAND" 即手牌, 表示玩家所持有的一系列字母, 玩家最初所持有的手牌将随机挑选.
我们将手牌描述为字典类型: 它的 `key` 是手牌字母, `value` 为该字母出现的次数.
这里注意当访问字典中一个不确定是否存在的 `key` 时, 为了避免 `KeyError`, 可以使用 `dict.get(key, default)` 方法.

```python
def getFrequencyDict(sequence):
    freq = {}
    for letter in sequence:
        freq[letter] = freq.get(letter,0) + 1   # 如果存在key "letter", 则它的值加 1, 否则初始化该 key 的值为 0 + 1
    return freq
```

这个部分完整的过程包括:
- converting words into dictionary representation - `getFrequencyDict(sequence)`
- displaying a hand - `displayHand(hand)`
- generating a random hand - `dealHand(n)`
- removing letters from a hand - `updateHand(hand, word)`

### P3 - Valid Words

实现函数 `isValidWord(word, hand, wordList)` 判断玩家输入的 `word` 是否有效,
一个有效单词应该属于 `wordList`, 并完全由当前 `hand` 中的字母构成.

### P4 - Hand Length

在实现整个游戏交互之前, 我们还需要实现辅助函数 `calculateHandlen(hand)` 计算手牌长度.
需要注意的是当某个字母出现多次的时候也要相应增加手牌长度.

### P5 - Playing a hand

参考以下伪码实现函数 `playHand(hand, wordList, n)`.

```
Keep track of the total score

As long as there are still letters left in the hand:

    Display the hand

    Ask user for input

    If the input is a single period:

        End the game (break out of the loop)


    Otherwise (the input is not a single period):

        If the word is not valid:

            Reject invalid word (print a message followed by a blank line)

        Otherwise (the word is valid):

            Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

            Update the hand


Game is over (user entered a '.' or ran out of letters), so tell user the total score

```

### P6 - Playing a Game

最后, 一个完整的游戏还需要可以玩多手, 实现 `playGame(wordList)` 来控制游戏进程.

```
Allow the user to play an arbitrary number of hands.

1) Asks the user to input 'n' or 'r' or 'e'.
  * If the user inputs 'n', let the user play a new (random) hand.
  * If the user inputs 'r', let the user play the last hand again.
  * If the user inputs 'e', exit the game.
  * If the user inputs anything else, tell them their input was invalid.

2) When done playing the hand, repeat from step 1

```


### P7 - Computer Chooses a Word

在 P1-P6 的基础上, 我们已经实现了一个完整的游戏交互流程, 之后的三个问题将进一步扩展该游戏的功能.
在 P7, 首先实现函数 `comChooseWord(hand, wordList, n)`, 伪码如下:

```
Create a new variable to store the maximum score seen so far (initially 0)

Create a new variable to store the best word seen so far (initially None)  

For each word in the wordList

    If you can construct the word from your hand
    (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

        Find out how much making that word is worth

        If the score for that word is higher than your best score

            Update your best score, and best word accordingly


return the best word you found.

```

### P8 && P9

实现了 P7 中的电脑选词功能后, 参考 `playHand` 和 `playGame`, 为计算机实现相应的流程.
