import pytest
from ansiconverter import converter, styles


# Tests for the converter module
def test_RGBtoHEX():
    assert converter.RGBtoHEX(13, 24, 128) == "#0d1880"


def test_RGBtoANSI_blank_list():
    with pytest.raises(ValueError) as e_info:
        converter.RGBtoANSI([])


def test_RgbtoAnsi_blank():
    assert converter.RGBtoANSI() == "\x1B[38;2;255;255;255m"

def test_HEXtoRGB():
    assert converter.HEXtoRGB("#1b815a") == [27, 129, 90]


def test_HEXtoRGB_shoterValue():
    with pytest.raises(ValueError) as e_info:
        converter.HEXtoRGB("#1b815")


def test_HEXtoRGB_longerValue():
    with pytest.raises(ValueError) as e_info:
        converter.HEXtoRGB("#1b815ad")


def test_HEXtoRGB_2sharp():
    assert converter.HEXtoRGB("##1b815a") == [27, 129, 90]


# Tests for the styles module

def test_styles_bold():
    assert styles.bold("Test") == "\x1b[1mTest\x1b[0m"
    
def test_styles_faint():
    assert styles.faint("Test") == "\x1b[2mTest\x1b[0m"

def test_styles_italic():
    assert styles.italic("Test") == "\x1b[3mTest\x1b[0m"
