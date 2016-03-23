# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples can both be composed of any types or values. Values are also in index form. However, different from lists and similar to strings, tuples cannot be changed. They are immutable.
- Dictionary keys are only compatible with immutable objects. This makes lists incompatible with dictionary keys. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> The only way lists and sets are similar is that they are both mutable, meaning they can be modified. They can also be iterated through. What makes them different is that sets cannot be indexed, are unordered, there cannot be duplicates and can be manipulated using mathematical operations.

- Set:
```
my_set = set(['one', 'two'])
other_set = set(['two','three'])
my_set.update(other_set)
my_set
{'one','three','two'}
```
- List:
```
my_list = ('one','two')
other_list = ('two','three')
my_list + other_list
('one','two','two','three')
```
>> sets are the preferred alternative to performing computational operations or determining duplicates or matches. They might not, however, perform better when iterating. Lists are simplified.

---
###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Put simply, Lambda is an in-line function. It acomplishes the same thing as a `def` would, but it is just simplified in order to save time and space. They are a matter of style.

```
my_list = ['dog', 'cat', 'bird', 'ant']
sorted(my_list)
['ant','bird','cat','dog']
```
```
sorted(my_list, key=lambda my_list: my_list[-1])
['bird', 'dog', 'cat', 'ant']
```

---
###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions simplify your code by allowing you to skip the for loop and start creating lists, dicts, and sets straight from your iterables. It also allows you to create the equivalents of `map` and `filter` in a more pythonic way of programming.

#####Map
```
items = [1, 2, 3, 4, 5]
list(map((lambda x: x**2), items))
[1, 4, 9, 16, 25]
```
-list comprehension
```
S = [x**2 for x in items] 
```
#####Filter
```
list(flter((lambda x: x<3), items))
[1,2]
```
-list comprehension
```
V = [x for x in items if x<3]
```

>> Capabilities for both methonds are very similar and the final results are the same, however, the list comprehensions provide you with an easier route.

#####Set comprehension
```
[round(x/y) for y in range(1,11) for x in range(1,21)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

# a set comprhension will only keep unique values
{round(x/y) for y in range(1,11) for x in range(1,21)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}


```
#####Dictionary comprehension
```
# A fast way of creating dictionaries
{number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





