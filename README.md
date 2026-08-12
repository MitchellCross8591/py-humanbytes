# Human-readable byte sizes

```
humanbytes.py
```

Run the Python Humanbytes test next to the implementation for concrete examples.

Format byte counts as KB/MB/GB and parse them back — dependency-free.

Python Humanbytes uses only the python standard library; there is no service or dependency to install.

Here's the core idea: you have a number of bytes, and you want to show it as something a human can read without squinting. Same goes for the reverse — turn "1.5 GB" back into an integer. Both directions are covered, and both stick to what the standard library gives you.

The implementation is small enough to read in one sitting. No hidden state, no global config. You call a function, you get a string or an int back. That's the contract.

For formatting, the function picks the right unit based on powers of 1024. It rounds to two decimal places, which keeps the output tidy for both tiny files and large blobs. Parsing is the inverse: it splits the string, validates the unit, and multiplies. If the input is malformed, you get a clear error instead of a silent wrong answer.

Why bother? Because in production, you will eventually log a byte count or accept one from a config file. When that happens, you want the conversion to be predictable. This module makes it predictable, and it's trivial to test — the test file next to it exercises the edge cases you'd care about: zero bytes, negative values, fractional input, and unit boundaries.

If you need to adjust the precision or add a new unit, the code is short enough that the change is obvious. No magic, no surprises.