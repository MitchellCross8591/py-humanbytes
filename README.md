# Human-readable byte sizes

```
humanbytes.py
```
We added this after a recent postmortem. A queue consumer logged raw byte counts, making it impossible to triage disk pressure alerts from the logs. Run the Python Humanbytes test next to the implementation to verify the formatting logic.

The utility formats raw byte counts as KB, MB, or GB and parses those strings back into integers. Ensure your parsing logic remains idempotent when handling these conversions.

Python Humanbytes relies entirely on the standard library. There are no external packages to install and no backend services to configure.