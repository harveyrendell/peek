# Peek

#### Take a peek at your code in action

This module is inspired by [pry](https://github.com/pry/pry) for Ruby.

# Install

Install locally from source:

```
git clone https://github.com/Puhapig/peek.git
cd peek
pip install -e .
```

# Use

Simply drop the following snippet into your Python code to open an interactive
session at that point in time.

```python
import peek

# your code here

peek.at()

# rest of your code here
```

or for a one-liner:

```python
import peek; peek.at()
```
