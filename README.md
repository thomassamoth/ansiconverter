# ANSI Converter  

![PyPI](https://img.shields.io/pypi/v/ansiconverter) ![PyPI - License](https://img.shields.io/pypi/l/ansiconverter) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiconverter) ![PyPI - Status](https://img.shields.io/pypi/status/ansiconverter)

Convert any color to the ANSI format to write in colors in your terminal.

## Installation

Run this command to install `ansiconverter`:

```python
pip install ansiconverter
```

To install for **development**:

```bash
git clone https://github.com/thomassamoth/ansiconverter.git
cd ansiconverter
pip install -e .[dev]
```

## Usage

### Converter module

#### Convert any RGB color to ANSI

```python
# How to print a green text on a white background
from ansiconverter import converter as cv

print(
    f"{cv.RGBtoANSI(foregound=[0, 255, 0], background=[255, 255, 255])} \
      Green text on white background{cv.RESET}"
    )

# Alternative
duo = cv.RGBtoANSI(foregound=[0, 255, 0], background=[255, 255, 255])

print(f"{duo} Another green text on white bg {cv.RESET}")

```

#### Convert any hexadecimal color to ANSI  

> **Warning**: no background color available for now

```python
# How to print a yellow text with its hexadeciaml value
from ansiconverter import converter as cv

print(f"{cv.HEXtoANSI('#f6cf6c')}Some yellow text{cv.RESET}")

```

### Styles module

Write your text in different styles :

* bold
* italic
* faint
* underlined
* bold & underlined
* strikethrough
* reversed

```python

from ansiconverter import styles

print(styles.bold("Some text in bold"))
```

### Combination of colors and styles

It is possible to combine text styles with colors by doing so:

```python
from ansiconverter import converter, styles

yellow = converter.HEXtoANSI('#f6cf6c')

print(styles.bold(yellow+"A text in yellow,bold and italic"+styles.RESET))
```

You can even combine **different styles** with a color :

```python
print(styles.bold(styles.italic(yellow+"A text in yellow,bold and italic"+styles.RESET)))
```

**Result:**  

<img src="https://user-images.githubusercontent.com/25958977/188747345-e234fb0b-a0c5-4a97-8fc6-f0081b105799.png" height=50, width=650> 

You can replace `styles.bold()` by any function mentionned [above](#styles-module) i.e. `styles.italic()`.

## Additional utilities

You can also use RGB to HEX converter or HEX to RGB by themselves like this:

``` python
>>>from ansiconverter import converter

>>> print(converter.HEXtoRGB("#0b38c1"))
[11, 59, 193])

>>> print(converter.RGBtoHEX([11, 59, 193]))
"#0b3bc1"
```

* * *

**Note:** This repository is based on [Mark Smith](https://github.com/judy2k)'s talk available [here](https://youtu.be/GIF3LaRqgXo) and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)
