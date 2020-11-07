# Tape
Tape tracks function calls so developers know when and how their code is used.

## An example
You invented a new method called `add_one`:
```python
# add.py
def add_one(x):
    return x + 1
```
You'd like to know when `add_one` is invoked by users. 

You can find out how often its invoked by adding a single Tape decorator:
```python
# add.py
from Tape import tape

@tape("add_package")
def add_one(x):
    return x + 1
```
That's it. Going forward, future invocations of `add_one` are logged.

Importantly, the end user experience remains unchanged:
```python
# from the user's perspective
from add import add_one
add_one(2)  # returns 3
```
### Querying
Tabulated counts can be retrieved with:
```bash
curl -i "http://localhost:5000/api?package=add_package&func=add_one"
```

## Install
```bash
git clone https://github.com/mynameisvinn/Tape
python setup.py install
```

