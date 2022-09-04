# ansiconverter  

Convert any color to the ANSI format to write in colors in your terminal.

## Installation

Run this command to install ansiconverter:

```python
pip install ansiconverter
```

##  Usage

### Converter module

#### Convert any RGB color to ANSI

```python
# How to print a green text on a white background
from ansiconverter import converter as cv

print(f"{cv.RGBtoANSI(foregound=[0, 255, 0], background=[255, 255, 255])}Green text on white background{cv.RESET}")

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

**Note :** This repository is based on [@judy2k](https://github.com/judy2k)'s talk available [here](https://youtu.be/GIF3LaRqgXo) and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)
