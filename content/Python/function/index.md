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
subtitle: function
summary: Learn how to blog in Academic using Jupyter notebooks
tags: []
title: function 

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
    

##    多個回傳值


```python
def f():
    a = 5
    b = 6
    c = 7
    return a,b,c

return_value = f()

# return value 就是3-tuple
return_value


```




    (5, 6, 7)



另一種方法回傳多個值,就是回傳dict:


```python
def f():
    a = 5
    b = 6
    c = 7
    return{'a': a ,'b': b ,'c': c}

return_value = f()

return_value
```




    {'a': 5, 'b': 6, 'c': 7}



## Functions Are Objects

假設我們要對以下字串list做一些清理和轉換的工作,像是去除空白,刪除標點符號,統一大小寫等


```python



states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda','south carolina##', 'West virginia?']

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()                  #刪除空白
        value = re.sub('[!#?]', '', value)     #替換特殊符號
        value = value.title()                  #title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始
        result.append(value)
    return result

```


```python
clean_strings(states)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



另一個有用的方法,是將要做的動作寫成list,然後對你想修改的字串使用這些動作:


```python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```


```python
clean_strings(states, clean_ops)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



你可以將一個函式當作另一個函式的參數,例如內建的 map 函式 


```python
for x in map(remove_punctuation, states):
    print(x)
    
map(remove_punctuation, states)
```

     Alabama 
    Georgia
    Georgia
    georgia
    FlOrIda
    south carolina
    West virginia
    




    <map at 0x197a79d5b70>



 ## 匿名函式


```python
def short_function(x):
    return x * 2
```

寫法同下 :


```python
equiv_anon = lambda x: x * 2
```

範例:


```python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [8, 0, 2, 10, 12]




```python
def apply_to_list(some_list, f):
    return f(some_list)

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [4, 0, 1, 5, 6, 4, 0, 1, 5, 6]



我們也可以將lambda函式傳到list的sort方法中


```python
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```


```python
strings.sort(key=lambda x: len(set(list(x))))

strings
```

## Generators (產生器)

Having a consistent way to iterate over sequences, like objects in a list or lines in a
file, is an important Python feature. This is accomplished by means of the iterator
protocol, a generic way to make objects iterable. For example, iterating over a dict
yields the dict keys:


```python
some_dict = {'a': 1, 'b': 2, 'c': 3}

for key in some_dict:
    print(key)
```

    a
    b
    c
    

When you write for key in some_dict, the Python interpreter first attempts to create
an iterator out of some_dict:


```python
dict_iterator = iter(some_dict)
dict_iterator
```




    <dict_keyiterator at 0x197a7a520e8>



An iterator is any object that will yield objects to the Python interpreter when used in
a context like a for loop. Most methods expecting a list or list-like object will also
accept any iterable object. This includes built-in methods such as min, max, and sum,
and type constructors like list and tuple:
    
A generator is a concise way to construct a new iterable object. Whereas normal functions
execute and return a single result at a time, generators return a sequence of
multiple results lazily, pausing after each one until the next one is requested. To create
a generator, use the yield keyword instead of return in a function:


```python
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2 
```

When you actually call the generator, no code is immediately executed:


```python
gen = squares()
gen
```




    <generator object squares at 0x00000197A7A68620>



It is not until you request elements from the generator that it begins executing its
code:


```python
for x in gen:
    print(x, end=' ')
```

    Generating squares from 1 to 100
    1 4 9 16 25 36 49 64 81 100 

## Generator expresssions

另一種製造產生器的簡單方法是利用Generator expresssions ,寫在小括號中:


```python
gen = (i** 2 for i in range(100))

gen
```




    <generator object <genexpr> at 0x00000197A7A68B48>



以上寫法完全等同於以下寫法:


```python
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

gen
```




    <generator object _make_gen at 0x00000197A7A685C8>



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
    

##    多個回傳值


```python
def f():
    a = 5
    b = 6
    c = 7
    return a,b,c

return_value = f()

# return value 就是3-tuple
return_value


```




    (5, 6, 7)



另一種方法回傳多個值,就是回傳dict:


```python
def f():
    a = 5
    b = 6
    c = 7
    return{'a': a ,'b': b ,'c': c}

return_value = f()

return_value
```




    {'a': 5, 'b': 6, 'c': 7}



## Functions Are Objects

假設我們要對以下字串list做一些清理和轉換的工作,像是去除空白,刪除標點符號,統一大小寫等


```python



states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda','south carolina##', 'West virginia?']

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()                  #刪除空白
        value = re.sub('[!#?]', '', value)     #替換特殊符號
        value = value.title()                  #title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始
        result.append(value)
    return result

```


```python
clean_strings(states)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



另一個有用的方法,是將要做的動作寫成list,然後對你想修改的字串使用這些動作:


```python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```


```python
clean_strings(states, clean_ops)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



你可以將一個函式當作另一個函式的參數,例如內建的 map 函式 


```python
for x in map(remove_punctuation, states):
    print(x)
    
map(remove_punctuation, states)
```

     Alabama 
    Georgia
    Georgia
    georgia
    FlOrIda
    south carolina
    West virginia
    




    <map at 0x197a79d5b70>



 ## 匿名函式


```python
def short_function(x):
    return x * 2
```

寫法同下 :


```python
equiv_anon = lambda x: x * 2
```

範例:


```python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [8, 0, 2, 10, 12]




```python
def apply_to_list(some_list, f):
    return f(some_list)

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [4, 0, 1, 5, 6, 4, 0, 1, 5, 6]



我們也可以將lambda函式傳到list的sort方法中


```python
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```


```python
strings.sort(key=lambda x: len(set(list(x))))

strings
```

## Generators (產生器)

Having a consistent way to iterate over sequences, like objects in a list or lines in a
file, is an important Python feature. This is accomplished by means of the iterator
protocol, a generic way to make objects iterable. For example, iterating over a dict
yields the dict keys:


```python
some_dict = {'a': 1, 'b': 2, 'c': 3}

for key in some_dict:
    print(key)
```

    a
    b
    c
    

When you write for key in some_dict, the Python interpreter first attempts to create
an iterator out of some_dict:


```python
dict_iterator = iter(some_dict)
dict_iterator
```




    <dict_keyiterator at 0x197a7a520e8>



An iterator is any object that will yield objects to the Python interpreter when used in
a context like a for loop. Most methods expecting a list or list-like object will also
accept any iterable object. This includes built-in methods such as min, max, and sum,
and type constructors like list and tuple:
    
A generator is a concise way to construct a new iterable object. Whereas normal functions
execute and return a single result at a time, generators return a sequence of
multiple results lazily, pausing after each one until the next one is requested. To create
a generator, use the yield keyword instead of return in a function:


```python
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2 
```

When you actually call the generator, no code is immediately executed:


```python
gen = squares()
gen
```




    <generator object squares at 0x00000197A7A68620>



It is not until you request elements from the generator that it begins executing its
code:


```python
for x in gen:
    print(x, end=' ')
```

    Generating squares from 1 to 100
    1 4 9 16 25 36 49 64 81 100 

## Generator expresssions

另一種製造產生器的簡單方法是利用Generator expresssions ,寫在小括號中:


```python
gen = (i** 2 for i in range(100))

gen
```




    <generator object <genexpr> at 0x00000197A7A68B48>



以上寫法完全等同於以下寫法:


```python
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

gen
```




    <generator object _make_gen at 0x00000197A7A685C8>



# 可變動與不可變動型別:

<img alt="" class="nm nn gp n o go x gm" width="658" height="308" role="presentation" src="https://miro.medium.com/max/823/1*uFlTNY4W3czywyU18zxl8w.png">

## 重點

## 1. mutable type 使用 [:] 複製元素,元素各自獨立


```python
a = [1,2]
c = [a[:] for x in range(2)]
c[0][0] = 3
c
```




    [[3, 2], [1, 2]]



### 以下為錯誤示範


```python
#錯誤
a = [3,4]
b = [a]*2
a[1] = 8
b

```




    [[3, 8], [3, 8]]




```python
#正確
a = [3,4]
c = [a[:]]*2
a[1] = 8
c

```




    [[3, 4], [3, 4]]



#### for 迴圈 與 串列
#### 1.  使用下標：透過len取得串列長度
#### 2  直接取得元素


```python
#使用下標

a = [5,8,7]
for i in range( len(a)):
    print(a[i])
```

    5
    8
    7
    


```python
# 直接取得元素
a = [5,8,7]
for x in a:
    print(x)
```

    5
    8
    7
    

### for 迴圈更改串列元素


```python
a = [1,8,3]
for i in range(len(a)):
    a[i] += 10
a
```




    [11, 18, 13]



以下為錯誤用法 : 因為整數為immutable


```python
## 錯誤示範

a = [1,8,3]
for x in a:
    x += 10    

```




    [1, 8, 3]



## 2. 函式參數值的更改 
 - immutable 參數在函式內的更動會變換儲存位置,與原本傳入的變數脫離關係
 - mutable 參數在函式內的更動不會變換儲存位置,會影響原傳入變數


```python
# a 為 immutable , b為 mutable
def change_vals(a,b):
    print(a)
    a = 10            # a 另找空間儲存10, a與 foo脫離關係
    b.append(5)       # b 串列增加一個元素
    
foo , bar = 3, [4,9]

#在函式內變更二參數資料

change_vals(foo,bar)

#foo 整數不變 , bar串列會變動

print(foo , bar )    # A : foo =3 ,bar =[4,9,5]
```

- immutable 參數可透過函式回傳來變更


```python
def inc_one (s , t):
    s += 1
    t += 1
    return s,t

a , b = 2,5
a,b = inc_one(a,b)
a,b
```




    (3, 6)



- 串列參數若指定到新串列,之後的設定不影響原傳入串列


```python
def change_lists(a,b):
    a =[3]                  # a 指定到新串列,與原傳入串列 foo 脫離關係
    b[0] = 5                # 修改 b[0] 元素

foo , bar =[9], [2,7]

change_lists(foo,bar)

print(foo,bar)
```

    [9] [5, 7]
    

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
    

##    多個回傳值


```python
def f():
    a = 5
    b = 6
    c = 7
    return a,b,c

return_value = f()

# return value 就是3-tuple
return_value


```




    (5, 6, 7)



另一種方法回傳多個值,就是回傳dict:


```python
def f():
    a = 5
    b = 6
    c = 7
    return{'a': a ,'b': b ,'c': c}

return_value = f()

return_value
```




    {'a': 5, 'b': 6, 'c': 7}



## Functions Are Objects

假設我們要對以下字串list做一些清理和轉換的工作,像是去除空白,刪除標點符號,統一大小寫等


```python



states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda','south carolina##', 'West virginia?']

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()                  #刪除空白
        value = re.sub('[!#?]', '', value)     #替換特殊符號
        value = value.title()                  #title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始
        result.append(value)
    return result

```


```python
clean_strings(states)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



另一個有用的方法,是將要做的動作寫成list,然後對你想修改的字串使用這些動作:


```python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```


```python
clean_strings(states, clean_ops)
```




    ['Alabama',
     'Georgia',
     'Georgia',
     'Georgia',
     'Florida',
     'South Carolina',
     'West Virginia']



你可以將一個函式當作另一個函式的參數,例如內建的 map 函式 


```python
for x in map(remove_punctuation, states):
    print(x)
    
map(remove_punctuation, states)
```

     Alabama 
    Georgia
    Georgia
    georgia
    FlOrIda
    south carolina
    West virginia
    




    <map at 0x197a79d5b70>



 ## 匿名函式


```python
def short_function(x):
    return x * 2
```

寫法同下 :


```python
equiv_anon = lambda x: x * 2
```

範例:


```python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [8, 0, 2, 10, 12]




```python
def apply_to_list(some_list, f):
    return f(some_list)

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```




    [4, 0, 1, 5, 6, 4, 0, 1, 5, 6]



我們也可以將lambda函式傳到list的sort方法中


```python
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```


```python
strings.sort(key=lambda x: len(set(list(x))))

strings
```

## Generators (產生器)

Having a consistent way to iterate over sequences, like objects in a list or lines in a
file, is an important Python feature. This is accomplished by means of the iterator
protocol, a generic way to make objects iterable. For example, iterating over a dict
yields the dict keys:


```python
some_dict = {'a': 1, 'b': 2, 'c': 3}

for key in some_dict:
    print(key)
```

    a
    b
    c
    

When you write for key in some_dict, the Python interpreter first attempts to create
an iterator out of some_dict:


```python
dict_iterator = iter(some_dict)
dict_iterator
```




    <dict_keyiterator at 0x197a7a520e8>



An iterator is any object that will yield objects to the Python interpreter when used in
a context like a for loop. Most methods expecting a list or list-like object will also
accept any iterable object. This includes built-in methods such as min, max, and sum,
and type constructors like list and tuple:
    
A generator is a concise way to construct a new iterable object. Whereas normal functions
execute and return a single result at a time, generators return a sequence of
multiple results lazily, pausing after each one until the next one is requested. To create
a generator, use the yield keyword instead of return in a function:


```python
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2 
```

When you actually call the generator, no code is immediately executed:


```python
gen = squares()
gen
```




    <generator object squares at 0x00000197A7A68620>



It is not until you request elements from the generator that it begins executing its
code:


```python
for x in gen:
    print(x, end=' ')
```

    Generating squares from 1 to 100
    1 4 9 16 25 36 49 64 81 100 

## Generator expresssions

另一種製造產生器的簡單方法是利用Generator expresssions ,寫在小括號中:


```python
gen = (i** 2 for i in range(100))

gen
```




    <generator object <genexpr> at 0x00000197A7A68B48>



以上寫法完全等同於以下寫法:


```python
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

gen
```




    <generator object _make_gen at 0x00000197A7A685C8>



# 可變動與不可變動型別:

<img alt="" class="nm nn gp n o go x gm" width="658" height="308" role="presentation" src="https://miro.medium.com/max/823/1*uFlTNY4W3czywyU18zxl8w.png">

## 重點

## 1. mutable type 使用 [:] 複製元素,元素各自獨立


```python
a = [1,2]
c = [a[:] for x in range(2)]
c[0][0] = 3
c
```




    [[3, 2], [1, 2]]



### 以下為錯誤示範


```python
#錯誤
a = [3,4]
b = [a]*2
a[1] = 8
b

```




    [[3, 8], [3, 8]]




```python
#正確
a = [3,4]
c = [a[:]]*2
a[1] = 8
c

```




    [[3, 4], [3, 4]]



#### for 迴圈 與 串列
#### 1.  使用下標：透過len取得串列長度
#### 2  直接取得元素


```python
#使用下標

a = [5,8,7]
for i in range( len(a)):
    print(a[i])
```

    5
    8
    7
    


```python
# 直接取得元素
a = [5,8,7]
for x in a:
    print(x)
```

    5
    8
    7
    

### for 迴圈更改串列元素


```python
a = [1,8,3]
for i in range(len(a)):
    a[i] += 10
a
```




    [11, 18, 13]



以下為錯誤用法 : 因為整數為immutable


```python
## 錯誤示範

a = [1,8,3]
for x in a:
    x += 10    

```




    [1, 8, 3]



## 2. 函式參數值的更改 
 - immutable 參數在函式內的更動會變換儲存位置,與原本傳入的變數脫離關係
 - mutable 參數在函式內的更動不會變換儲存位置,會影響原傳入變數


```python
# a 為 immutable , b為 mutable
def change_vals(a,b):
    print(a)
    a = 10            # a 另找空間儲存10, a與 foo脫離關係
    b.append(5)       # b 串列增加一個元素
    
foo , bar = 3, [4,9]

#在函式內變更二參數資料

change_vals(foo,bar)

#foo 整數不變 , bar串列會變動

print(foo , bar )    # A : foo =3 ,bar =[4,9,5]
```

- immutable 參數可透過函式回傳來變更


```python
def inc_one (s , t):
    s += 1
    t += 1
    return s,t

a , b = 2,5
a,b = inc_one(a,b)
a,b
```




    (3, 6)



- 串列參數若指定到新串列,之後的設定不影響原傳入串列


```python
def change_lists(a,b):
    a =[3]                  # a 指定到新串列,與原傳入串列 foo 脫離關係
    b[0] = 5                # 修改 b[0] 元素

foo , bar =[9], [2,7]

change_lists(foo,bar)

print(foo,bar)
```

    [9] [5, 7]
    
