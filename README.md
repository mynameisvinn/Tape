# tapeworm
tapeworm tracks function calls so you can understand how code is used.


## example
you invented a new function called `add_one`:
```python
# add.py

def add_one(x):
    return x + 1
```
youd like to know when `add_one` is invoked by users. 

with tapeworm, you can find out by adding a single decorator to source:
```python
# add.py
from tapeworm import worm

@tape
def add_one(x):
    return x + 1
```
that's it. going forward, future invocations of `add_one` are logged.

importantly, the user experience remains unchanged:
```python
# from the user's perspective
from add import add_one

add_one(2)  # returns 3
```