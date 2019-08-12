---
authors:
- admin
categories: []
date: "2019-08-12T00:00:00Z"
draft: false
featured: false
image:
  caption: ""
  focal_point: ""
projects: []
subtitle: Learn how to blog in Academic using Jupyter notebooks
summary: Learn how to blog in Academic using Jupyter notebooks
tags: []
title: list 

---
## 返回值
When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:

+ The return keyword

+ The value or expression that the function should return 函數要返回的值或表示式


```python

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
```

    It is decidedly so
    

 # NONE 值
 
 print 值 返回 None 
 如同 r 的 side effect
 對於有沒有寫return陳述句的函數,python都會加上return None


```python
spam = print('Hello!')
None == spam
```

    Hello!
    




    True



## 區域變數不能使用在全域作用範圍內
(跟r一樣)



```python
def spam():
    eggs = 31337
spam()
print(eggs)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-c77831cffe5d> in <module>()
          2     eggs = 31337
          3 spam()
    ----> 4 print(eggs)
    

    NameError: name 'eggs' is not defined


## Local Scopes Cannot Use Variables in Other Local Scopes
The upshot is that local variables in one function are completely separate from the local variables in another function.


某個函式中的區域變數與其他函式中的區域變數是完全分開來的,就算名稱相同也完全不相干


```python
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    
spam()
```

    99
    

## gobal 陳述句

If you need to modify a global variable from within a function, use the global statement. If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.


```python
def spam():
    global eggs
    eggs = 'spam'

print(eggs)
```

    spam
    

There are four rules to tell whether a variable is in a local scope or global scope:

1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

2. If there is a global statement for that variable in a function, it is a global variable.

3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

4. But if the variable is not used in an assignment statement, it is a global variable.

for example:


```python
def spam():
    global eggs    
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)
```

    spam
    

In the spam() function, eggs is the global eggs variable, because there’s a global statement for eggs at the beginning of the function `1`. In bacon(), eggs is a local variable, because there’s an assignment statement for it in that function `2`. In ham() `3`, eggs is the global variable, because there is no assignment statement or global statement for it in that function. 

## 例外處理
python 程式中若有錯誤(error),或例外(exception)導致整個程式當掉,而我們並不希望發生這樣的事

ｅｘ：［除以０］


```python
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

    21.0
    3.5
    


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-15-cce18d473349> in <module>()
          4 print(spam(2))
          5 print(spam(12))
    ----> 6 print(spam(0))
          7 print(spam(1))
    

    <ipython-input-15-cce18d473349> in spam(divideBy)
          1 def spam(divideBy):
    ----> 2     return 42 / divideBy
          3 
          4 print(spam(2))
          5 print(spam(12))
    

    ZeroDivisionError: division by zero


利用try和except陳述句來處理,把有可能出錯的陳述句放在try子句當中,

當錯誤發生時,程式的執行會跳到接下來的except子句起始處

把前面除以0的程式碼放在try子句中,而except子句中寫入程式碼來處理錯誤發生時想要做的事


```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

    21.0
    3.5
    Error: Invalid argument.
    None
    42.0
    

## 小型例子 :猜數字遊戲


```python
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
```

    I am thinking of a number between 1 and 20.
    Take a guess.
    10
    Your guess is too high.
    Take a guess.
    1
    Your guess is too low.
    Take a guess.
    5
    Your guess is too low.
    Take a guess.
    8
    Your guess is too low.
    Take a guess.
    9
    Good job! You guessed my number in 5 guesses!
    
