# Tape
Tapeworm tracks function calls so you know when your code is used.

## An example
You invented a new function called `add_one`:
```python
# add.py

def add_one(x):
    return x + 1
```
You'd like to know when `add_one` is invoked by users. 

With Tape, you can find out by adding a single decorator to your method:
```python
# add.py
from Tapeworm import tape

@tape("mypackage")  # package name
def add_one(x):
    return x + 1
```
That's it. Going forward, future invocations of `add_one` are logged and counted.

Importantly, the end user experience remains unchanged:
```python
# from the user's perspective
from add import add_one

add_one(2)  # returns 3
```

Finally, you can query with:
```bash
curl -i "http://localhost:5000/api?package=mypackage&func=add_one"
```

## install
```bash
git clone https://github.com/mynameisvinn/Tape
python setup.py install
```

