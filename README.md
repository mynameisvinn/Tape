# Tape
Tape tracks function calls so developers know when and how their code is used. 

## An example
You invented a new method called `add_one`:
```python
# add.py
def add_one(x):
    return x + 1
```
You'd like to know when `add_one` is invoked by users. After all, just because you've open sourced your software doesn't mean you shouldn't know how it's used.

With Tape, you can simply add a `@tape` decorator to the function of interest:
```python
# add.py
from Tape import tape

@tape("add_package")  # <--- a single decorator is added
def add_one(x):
    return x + 1
```
And that's it. Going forward, invocations of `add_one` are logged and counted, even if it is executed remotely.

### User Experience is unchanged
Importantly, the end user experience remains identical:
```python
# from the user's perspective
from add import add_one

add_one(2)  # returns 3
```
### Querying
Tabulated counts can be retrieved:
```bash
curl -i "http://18.209.241.43:5000/api?package=add_package&func=add_one"  # youll need to know your package name and function name
```

## Install Tape
```bash
git clone https://github.com/mynameisvinn/Tape
python setup.py install
```

