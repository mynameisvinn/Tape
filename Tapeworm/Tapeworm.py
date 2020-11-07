import inspect
import hashlib
import requests


def tape(package_name):
    print("package name:", package_name)
    def mid(func):
        def inner(x):
            metadata = _extract(func)
            _push(metadata)
            return func(x)
        return inner
    return mid


def _extract(func):
    """extract metadata from code object.
    """
    func_name = func.__name__
    source = inspect.getsource(func)
    key = hashlib.sha256(source.encode('utf-8')).hexdigest()
    return {"func_name": func_name, "source": source, "key": key}


def _push(data):
    try:
        res = requests.put("http://localhost:5000/api", json=data)
    except:
        pass
