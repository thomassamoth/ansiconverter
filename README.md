# ansiconverter  

![PyPI](https://img.shields.io/pypi/v/ansiconverter) ![PyPI - License](https://img.shields.io/pypi/l/ansiconverter) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiconverter) ![PyPI - Status](https://img.shields.io/pypi/status/ansiconverter)

Convert any color to the ANSI format to write in colors in your terminal.

## Installation

Run this command to install ansiconverter:

```python
python -m pip install -U ansiconverter
```

##  :computer: Usage

### Converter module

#### Convert any RGB color to ANSI

```python
# How to print a green text on a white background
from ansiconverter.converter import RGBtoANSI

print(RGBtoANSI(text='Green text on a white background',foregound=[0, 255, 0], background=[255, 255, 255]))

```

#### Convert any hexadecimal color to ANSI  

> **Note:** Some colour combinations are incompatible, and the result will be slightly different from what is expected.

```python
# How to print a yellow text with its hexadeciaml value
from ansiconverter.converter import HEXtoANSI

print(HEXtoANSI('Some yellow text on blue background','#fdf31f', '000080'))

```

### :art: Styles module

Write your text in different styles :

* bold
* italic
* faint
* underlined
* bold & underlined
* strikethrough
* reversed

```python

from ansiconverter.styles import styles

print(styles.bold("Some text in bold"))
```

### Combination of colors and styles

It is possible to combine text styles with colors by doing so:

```python
from ansiconverter.converter import *
from ansiconverter.styles import styles

print(styles.bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))
```

You can replace `styles.bold()` by any function mentionned [above](#styles-module) i.e. `styles.italic()`.

## :heavy_plus_sign: Additional features

You can also use RGB to HEX converter or HEX to RGB by themselves like this:

``` python
>>> from ansiconverter import converter

>>> print(converter.HEXtoRGB("#0b38c1"))
[11, 59, 193])

>>> print(converter.RGBtoHEX([11, 59, 193]))
"#0b3bc1"
```

* * *

**Note:** This repository is based on [Mark Smith](https://github.com/judy2k)'s talk available [here](https://youtu.be/GIF3LaRqgXo) and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)
