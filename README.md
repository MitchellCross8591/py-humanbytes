# Human-readable byte sizes

```
humanbytes.py
```
We built this after a few too many pages caused by queue workers choking on misformatted payload sizes. You format raw byte counts into standard KB, MB, or GB strings. Then you parse those strings back into integers. The whole process is strictly dependency-free.

Run the Python Humanbytes test suite next to the implementation to see concrete examples. The module relies entirely on the standard library. You do not need to install external services or third-party packages to get this running in your environment.