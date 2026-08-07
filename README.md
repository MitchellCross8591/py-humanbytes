# Human-readable byte sizes

```
humanbytes.py
```

Run the Python Humanbytes test next to the implementation for concrete examples.

Format byte counts as KB/MB/GB and parse them back — dependency-free.

Python Humanbytes uses only the python standard library; there is no service or dependency to install.

If you've ever been woken up at 3 AM by a missed job because a size check overflowed an int, you know why this exists. The code is short, testable, and does exactly one thing: turn a raw byte count into something a human can read at a glance, and turn that string back into the number you started with.

The formatting side handles the usual units — KB, MB, GB — and picks the right one based on magnitude. Parsing does the reverse, accepting the output it produces and returning the exact byte count. Round-trip safe, so you can store the human-readable form and trust it.

No magic, no hidden state. Just functions you can call from a cron job, a queue worker, or a one-off script. The test file sits right next to the implementation, so you can see the expected behavior without digging through docs.

If you need to log sizes in a way that doesn't make your pager go off with a wall of digits, this is the tool. It won't fix your monitoring, but it'll make the alerts a little less painful to read.