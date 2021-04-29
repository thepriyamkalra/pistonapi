# Piston API Wrapper for Python

This is a very simple API Wrapper for the [Piston API](https://github.com/engineer-man/piston).  
The Piston API documentation can be found [here](https://github.com/engineer-man/piston#Public-API).


## Installation
```sh
pip install pistonapi
```

or
```sh
python setup.py build
python setup.py install
```


## Usage Example

```python
from pistonapi import PistonAPI

# Create a new Piston API instance
piston = PistonAPI()

# Get all the supported languages
print(piston.languages)
# OR
print(piston.runtimes)

# Execute your own code!
code = 'print("Hello, World!")'
print(piston.execute(language="py", version="3.9", code=code))
```
