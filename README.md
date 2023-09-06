# &#127744; ANSI Converter

![PyPI](https://img.shields.io/pypi/v/ansiconverter) ![PyPI - License](https://img.shields.io/pypi/l/ansiconverter) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiconverter) ![PyPI - Status](https://img.shields.io/pypi/status/ansiconverter)

Convert any colour to the [ANSI format](https://en.wikipedia.org/wiki/ANSI_escape_code) to write in colours in your terminal.

## &#9000; Installation

Run this command to install `ansiconverter`:

```bash
python -m pip install -U ansiconverter
```

To install for **development**:

```bash
git clone https://github.com/thomassamoth/ansiconverter.git
cd ansiconverter
pip install -e .[dev]
```
### Tests

To ensure the installation of this package has been successful, you can run the [tests](https://github.com/thomassamoth/ansiconverter/tree/main/test).

1. Make sure you installed the `pytest` module. Otherwise, run

```bash
pip install pytest
```
2. Install the package with the extra dev part 

```bash
pip install ansiconverter[dev]
```
3. To run the tests, execute

```bash
python -m pytest test/
```

##  &#128187; Usage

### Converter module

> &#9888;&#65039; **Warning**  
> Some colour combinations between background and foreground are incompatible. The result can be slightly different from what is expected.



<details>
<summary><strong>Convert from <i>RGB</i> colour to <i>ANSI</i></strong></summary>

```python
# How to print a green text on a white background
from ansiconverter.converter import RGBtoANSI
print(RGBtoANSI(text='Green text on a white background',foregound=[0, 255, 0], background=[255, 255, 255]))
```

**Result:**
<img src ="https://user-images.githubusercontent.com/25958977/190724022-a8b6e7cf-60e7-4493-9d9b-14b28be7268a.png" height=40 >
</details>  

<details>
<summary>
<strong>Convert from <i>hexadecimal</i> to <i>ANSI</i></strong>
</summary>

```python
# How to print a yellow text on a navy blue background, with hexadecimal values.
from ansiconverter.converter import HEXtoANSI

print(HEXtoANSI('Some yellow text on blue background','#fdf31f', '000080'))
```

**Result**:  
<img src="https://user-images.githubusercontent.com/25958977/190716452-69a8f8df-6f2d-4a79-94c2-f601dc4b4466.png" height=40)>  
</details>

> Another little tool has been added to convert RGB to hexadecimal and is not used to write in color in terminal but can be useful for other applications.

<details>
<summary>
<strong>Convert from <i>hexadecimal</i> to <i>RGB</i></strong>
</summary>

```python
from ansiconverter import converter
print(converter.HEXtoRGB("#0b38c1"))

>>> # Result :
[11, 59, 193]
```
</details>


<details>
<summary>
<strong>Convert from <i>RGB</i> to <i>hexadecimal</i></strong>
</summary>

```python
from ansiconverter import converter
print(converter.RGBtoHEX([11, 59, 193]))

>>> # Result :
"#0b3bc1"
```
</details>
<hr/>

### &#127912; Styles module 

Several text styles are available as well. You can even [combine them with colours](#⚗-combination-of-colours-and-styles)!

| Style                        | Method               |
|------------------------------|----------------------|
| bold                         | `bold`               |
| italic                       | `italic`             |
| fainted                      | `faint`              |
| underlined                   | `underline`          |
| bold & underlined            | `bold_and_underline` |
| strikethroughed              | `strikethrough`      |
| reversed _(colours inverted)_ | `reverse`            |


```python
from ansiconverter.styles import styles

print(bold("Some text in bold"))
```
Replace `.bold` in the example with any method above to get the desired style.  

<hr/>

### &#9879; Combination of colours and styles

It is possible to combine text styles with colours by doing so:

```python
from ansiconverter.converter import *
from ansiconverter.styles import styles

print(bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))
```

**Result:**  
<img src="https://user-images.githubusercontent.com/25958977/190715961-3a3da6e1-bf9f-4011-8644-29c3efa4f263.png"  height=40> 

**N.B**: the order between the style and the text format isn't important and you can switch them.

```python
print(bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))` 
```
will work the same as

```python
print(HEXtoANSI(bold('A yellow text in bold'),'#f6cf6c'))
```

## Note  

This structure of this repository is based on a talk by [Mark Smith](https://github.com/judy2k), which is available [here](https://youtu.be/GIF3LaRqgXo), and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)

