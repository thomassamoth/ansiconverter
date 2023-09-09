# &#127744; ANSI Converter

![PyPI](https://img.shields.io/pypi/v/ansiconverter) ![PyPI - License](https://img.shields.io/pypi/l/ansiconverter)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiconverter) ![PyPI - Status](https://img.shields.io/pypi/status/ansiconverter) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://makeapullrequest.com) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Convert any colour to the [ANSI format](https://en.wikipedia.org/wiki/ANSI_escape_code) to write in colours in your terminal.

## &#9000;&#65039; Installation

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

1. Make sure you have installed the `pytest` module. Otherwise, run:

```bash
pip install pytest
```

2. After you downloaded the code and installed the package, run the tests by executing:

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
from ansiconverter import RGBtoANSI
print(RGBtoANSI(text='Green text on a white background',foregound=[0, 255, 0], background=[255, 255, 255]))
```
**Result:**

**Result**:  
<img src ="https://github.com/thomassamoth/ansiconverter/assets/25958977/76d6d253-4176-4891-adae-8df05e56d62f" height=50 >
</details>  

<details>
<summary>
<strong>Convert from <i>hexadecimal</i> to <i>ANSI</i></strong>
</summary>

```python
# How to print a yellow text on a navy blue background, with hexadecimal values.
from ansiconverter import HEXtoANSI
print(HEXtoANSI('Some yellow text on blue background','#fdf31f', '000080'))
```
**Result**:

**Result**:  
<img src="https://github.com/thomassamoth/ansiconverter/assets/25958977/40954308-5be6-4e69-b8a8-c08a63224a03" height=50)>  
</details>

> &#8505;&#65039; **Note**  
> Another little tool has been added to convert RGB to hexadecimal and vice versa. It can't be used to write in color in the terminal but could be useful for other applications.

<details>
<summary>
<strong>Convert from <i>hexadecimal</i> to <i>RGB</i></strong>
</summary>

```python
from ansiconverter import HEXtoRGB
print(HEXtoRGB("#0b38c1"))
```

**Result** :
```python
[11, 59, 193]
```
</details>


<details>
<summary>
<strong>Convert from <i>RGB</i> to <i>hexadecimal</i></strong>
</summary>

```python
from ansiconverter import RGBtoHEX
print(RGBtoHEX([11, 59, 193]))
```

**Result** :
```python
"#0b3bc1"
```
</details>
<hr/>

### &#127912; Styles module 

Several text styles are available as well. You can even [combine them with colours](#combination-of-colours-and-styles)

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
from ansiconverter import bold

print(bold("Some text in bold"))
```
Replace `.bold` in the example with any method above to get the desired style.  

<hr/>

### Combination of colours and styles

 &#9879;&#65039; It is possible to combine text styles with colours by doing so:

```python
from ansiconverter import HEXtoANSI, bold
print(bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))
```

**Result:**  
<img src="https://github.com/thomassamoth/ansiconverter/assets/25958977/4936657f-a536-497e-b8da-4df1d8f53813"  height=50> 

**N.B**: the order between the style and the text format isn't important and you can switch them.

```python
print(bold(HEXtoANSI('A yellow text in bold','#f6cf6c')))
```
#

will work the same as

```python
print(HEXtoANSI(bold('A yellow text in bold'),'#f6cf6c'))
```

## Note  

This structure of this repository is based on a talk by [Mark Smith](https://github.com/judy2k), which is available [here](https://youtu.be/GIF3LaRqgXo), and its [linked repository](https://github.com/judy2k/publishing_python_packages_talk)

## License
This repository is licensed under the MIT license. See the [LICENSE](LICENSE.md) file for more information.
