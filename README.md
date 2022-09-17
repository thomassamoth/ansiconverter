# &#127744; ANSI Converter

![PyPI](https://img.shields.io/pypi/v/ansiconverter) ![PyPI - License](https://img.shields.io/pypi/l/ansiconverter) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiconverter) ![PyPI - Status](https://img.shields.io/pypi/status/ansiconverter)

Convert any colour to the ANSI format to write in colours in your terminal.

## &#9000; Installation

Run this command to install `ansiconverter`:

```python
python -m pip install -U ansiconverter
```

To install for **development**:

```bash
git clone https://github.com/thomassamoth/ansiconverter.git
cd ansiconverter
pip install -e .[dev]
```

##  &#128187; Usage

### Converter module

#### Convert any *RGB* colour to *ANSI*  

```python
# How to print a green text on a white background
from ansiconverter.converter import RGBtoANSI
print(RGBtoANSI(text='Green text on a white background',foregound=[0, 255, 0], background=[255, 255, 255]))

```
**Result:**

<img src ="https://user-images.githubusercontent.com/25958977/190724022-a8b6e7cf-60e7-4493-9d9b-14b28be7268a.png" width=700 >

#### Convert any *hexadecimal* colour to *ANSI*  

> **Warning**  
Some colour combinations are incompatible, and the result will be [slightly different](#convert-any-rgb-colour-to-ansi) from what is expected.

```python
# How to print a yellow text on a navy blue background, with hexadecimal values.
from ansiconverter.converter import HEXtoANSI

print(HEXtoANSI('Some yellow text on blue background','#fdf31f', '000080'))

```
**Result**:

<img src="https://user-images.githubusercontent.com/25958977/190716452-69a8f8df-6f2d-4a79-94c2-f601dc4b4466.png" width=700)>  

### Styles module &#127912;

Write your text in different styles:

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

### &#9879; Combination of colours and styles

It is possible to combine text styles with colours by doing so:

```python
from ansiconverter.converter import *
from ansiconverter.styles import styles

print(styles.bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))

```

**Result:**  

<img src="https://user-images.githubusercontent.com/25958977/190715961-3a3da6e1-bf9f-4011-8644-29c3efa4f263.png" width=700> 

You can replace `styles.bold()` by any function mentionned [above](#styles-module) i.e. `styles.italic()`. You can even **combine** different styles!

## &#10133; Additional features

You can also use ***RGB to HEX*** converter or ***HEX to RGB*** by themselves like this:

``` python
>>> from ansiconverter import converter

>>> print(converter.HEXtoRGB("#0b38c1"))
[11, 59, 193])

>>> print(converter.RGBtoHEX([11, 59, 193]))
"#0b3bc1"
```
#

> **Note**  
This repository is based on [Mark Smith](https://github.com/judy2k)'s talk available [here](https://youtu.be/GIF3LaRqgXo) and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)
