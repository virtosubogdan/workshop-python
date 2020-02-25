#### This is a presentation

To start:
```bash
npm install -g reveal-md
reveal-md README.md -W --css style.css
```

---
#### Python Workshop

* Establishing goals
* Python intro

Notes:
Expectations:
Refresh for python code
Better understanding on how python works
Better understanding on python code
Learning something new
How JS maps to Python
Less interested in OOP, functional programming, common concepts

Expectations nice to have:
Can do backend reviews
Django

---

### Python

* High-level
* Object-oriented
* Interpreted
* Dynamic
* Open source

---

### High level

* No memory or system management
* Expressive
* Powerful

```python
  import os
  from os.path import join, getsize

  for root, dirs, files in os.walk('.'):
    print(root, " consumes ", end="")
    print(sum([getsize(join(root, name)) for name in files]))
    print(" bytes in ", len(files), " non-directory files")

```

Notes:
test lba

---    

### Interpreted

* REPL, code is an object, dis, inspect
* Debugging

--- 

### Dynamic

* Dynamic typing
* Strong typing

---

### Object oriented

* Everything is an object
* Classes
* [Functional aspects](https://docs.python.org/3/howto/functional.html)


---

### Open Source

* [PEP](https://www.python.org/dev/peps/)
* [Core Developers](https://discuss.python.org/t/official-list-of-core-developers/924)
* [Packages Comparison](http://www.modulecounts.com/)
* [Code Status](https://www.openhub.net/p/python)

----

### History

----

<!-- .slide: data-background="https://i.imgur.com/uUspnyQ.png" -->

----

Fast changing versions

[Wiki History_of_Python#Table_of_versions](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions)

Notes:
understand vs learn

---

### Disadvantages

* Speed
* Age
* Driven by corporation aka consensus +/-
