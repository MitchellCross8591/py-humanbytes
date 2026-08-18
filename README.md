# Human-readable byte sizes

```
humanbytes.py
```
We built this to format and parse byte counts without pulling in heavy third-party modules. When your queue workers fail on edge-case string parsing, you want zero external dependencies in the critical path.

Run the Python Humanbytes test next to the implementation to see the exact formatting behavior. It handles KB, MB, and GB conversions and parses them back deterministically.

The module relies entirely on the standard library. There are no external services or packages to install. Keep your deployment artifacts small and ensure your parsing logic remains idempotent across restarts.