import inspect
import collections

try:
    import builtins as BuiltIns
except ImportError:
    import builtins as BuiltIns


pythonGlobals = {}

def populateGlobals():
    d = BuiltIns.__dict__
    for x in d:
        try:
            vx = d.get(x)
            if  inspect.isclass(vx) and issubclass(vx, BaseException):
                continue
            if isinstance(vx, collections.Callable):
                pythonGlobals[x] = vx
        except Exception:
            continue

populateGlobals()
