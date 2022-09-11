import pytest
from ansiconverter.converter import *
# from ansiconverter import styles
from ansiconverter.styles import styles


# Tests for the converter module


def test_RGBtoHEX():
    assert RGBtoHEX([13, 24, 128]) == "#0d1880"


def test_RGBtoANSI_blank_list():
    with pytest.raises(ValueError) as e_info:
        RGBtoANSI("text", [])


def test_RgbtoAnsi_blank():
    assert RGBtoANSI("text") == "\x1B[38;2;255;255;255mtext\x1b[0m"


def test_HEXtoRGB():
    assert HEXtoRGB("#1b815a") == [27, 129, 90]


def test_HEXtoRGB_shorterValue():
    with pytest.raises(ValueError) as e_info:
        HEXtoRGB("#1b815")


def test_HEXtoRGB_longerValue():
    with pytest.raises(ValueError) as e_info:
        HEXtoRGB("#1b815ad")


def test_HEXtoRGB_2sharp():
    assert HEXtoRGB("##1b815a") == [27, 129, 90]


# Tests for the styles module


def test_styles_bold():
    assert styles.bold("Test") == "\x1b[1mTest\x1b[0m"


def test_styles_faint():
    assert styles.faint("Test") == "\x1b[2mTest\x1b[0m"


def test_styles_italic():
    assert styles.italic("Test") == "\x1b[3mTest\x1b[0m"
