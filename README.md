
[![CircleCI](https://circleci.com/gh/ylathouris/bio.svg?style=shield)](https://circleci.com/gh/ylathouris/bia)  ![Coverage](coverage.svg)

---

# Code Bio

The `bio` package provides utilities for profiling python code. 

* [Decorator](#decorator.profile)
* [Context Manager](#contextmanager.profiler)

</br>

## Installation

```
pip install bio
```

</br>

### <a name="decorator.profile"></a>Decorator

```python
import bio

@bio.profile()
def my_functon():
    # Do stuff here
```

Using the `@bio.profile()` decorator with no arguments will simply print 
the output to `stdout`. Alternatively, you can provide the file location 
for the profiler output.

```python
@bio.profile("/path/to/file.prof")
def my_functon():
    # Do stuff here
```

In the example shown above, the output will be written to both `stdout` 
and the given file location. If you would prefer not to write to `stdout` 
you can use the `quiet=True` option.

```python
@bio.profile("/path/to/file.prof", quiet=True)
def my_functon():
    # Do stuff here
```

</br>


### <a name="conextmanager.profiler"></a>Context Manager

```python
import bio

with bio.profiler("/path/to/file.prof"):
    # Do stuff here
```

</br>

### <a name="testing"></a>Testing

Bio uses `tox` for testing. To run the tests, simply run:

```
tox
```