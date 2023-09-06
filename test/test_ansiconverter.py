import pytest
from ansiconverter import *


class TestsConverter:
    """Tests for the converter module"""

    def test_RGBtoHEX_valid_input(self):
        """Test the conversion from RGB to HEX with a correct list of colours"""
        assert RGBtoHEX([13, 24, 128]) == "#0d1880"

    def test_RGBtoANSI_blank_list(self):
        """Test the conversion from RGB to ANSI with no argument. It should raise an error"""
        with pytest.raises(ValueError) as e_info:
            RGBtoANSI("text", [])

    def test_RGBtoANSI_valid_input(self):
        """Test RGB to ANSI with a valid text"""
        assert RGBtoANSI("Valid Input") == "\x1B[38;2;255;255;255mValid Input\x1b[0m"

    def test_HEXtoRGB_valid_input(self):
        """Test from HEX to RGB with a correct string"""
        assert HEXtoRGB("#1b815a") == [27, 129, 90]

    def test_HEXtoRGB_shorter_value(self):
        """Test from HEX to RGB with string shorter than 6 characters"""
        with pytest.raises(ValueError) as e_info:
            HEXtoRGB("#1b815")

    def test_HEXtoRGB_longerValue(self):
        """Test from HEX to RGB with string longer than 6 characters"""
        with pytest.raises(ValueError) as e_info:
            HEXtoRGB("#1b815ad")

    def test_HEXtoRGB_2_sharp(self):
        """Test from HEX to RGB with 2 # entered (i.e after a copy/paste)"""
        assert HEXtoRGB("##1b815a") == [27, 129, 90]
        
    def test_RGBtoANSI_background(self):
        assert RGBtoANSI("Test", [0, 10, 24], [255, 255, 255]) == f"\033[38;2;{0};{10};{24}m\033[48;2;{255};{255};{255}mTest\x1b[0m"

    def test_HEXtoANSI_valid_input(self):
        assert HEXtoANSI("Test HEX to ANSI", "#fdd374")
        
    def test_HEXtoANSI_no_foreground(self):
        with pytest.raises(ValueError) as error:
            HEXtoANSI("Text", "")

class TestsStyles:
    """Tests for the style module"""

    def test_styles_bold(self):
        assert bold("Test") == "\x1b[1mTest\x1b[0m"

    def test_styles_italic(self):
        assert italic("Test") == "\x1b[3mTest\x1b[0m"

    def test_styles_faint(self):
        assert faint("Test") == "\x1b[2mTest\x1b[0m"

    def test_styles_underline(self):
        assert underline("Test") == "\x1b[4mTest\x1b[0m"

    def test_styles_bold_and_underline(self):
        assert bold_and_underline("Test") == "\x1b[1;4mTest\x1b[0m"

    def test_styles_strikethrough(self):
        assert strikethrough("Test strikethrough") == "\x1b[9mTest strikethrough\x1b[0m"

    def test_styles_reverse(self):
        assert reverse("Test reverse") == "\x1b[7mTest reverse\x1b[0m"

    def test_styles_combinations(self):
        assert HEXtoRGB("fef86c") == [254, 248, 108]
        assert bold(HEXtoANSI("Yellow", 'fef86c')) == '\x1b[1m\x1b[38;2;254;248;108mYellow\x1b[0m\x1b[0m'
        assert HEXtoANSI(bold("Yellow"), 'fef86c') == '\x1b[38;2;254;248;108m\x1b[1mYellow\x1b[0m\x1b[0m'