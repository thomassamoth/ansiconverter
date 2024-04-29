import pytest
from ansiconverter import *


class TestsConverter:
    """Tests for the converter module."""

    def test_RGBtoHEX_valid_input(self):
        """Test the conversion from RGB to HEX with a correct list of colours"""
        assert RGBtoHEX((13, 24, 128)) == "#0d1880"
        
    def test_RGBtoHEX_list_input(self):
        """Test the conversion from RGB to HEX with a correct list of colours"""
        assert RGBtoHEX([13, 24, 128]) == "#0d1880"

    def test_RGBtoHEX_out_of_range_value(self):
        with pytest.raises(ValueError) as e:
            RGBtoHEX((355, -2, 256))
        
    def test_RGBtoANSI_blank_list(self):
        """Test the conversion from RGB to ANSI with no argument. It should raise an error"""
        with pytest.raises(ValueError) as e:
            RGBtoANSI("text", ())

    def test_RGBtoANSI_valid_input(self):
        """Test RGB to ANSI with a valid text and no foreground color. (If printed text appears white.)
        """
        assert RGBtoANSI("Valid Input", (125, 125, 125)) == "\x1B[38;2;125;125;125mValid Input\x1b[0m"

    def test_HEXtoRGB_valid_input(self):
        """Test from HEX to RGB with a correct string"""
        assert HEXtoRGB("#1b815a") == (27, 129, 90)

    def test_HEXtoRGB_shorter_value(self):
        """Test from HEX to RGB with string shorter than 6 characters"""
        with pytest.raises(ValueError) as e:
            HEXtoRGB("#1b815")

    def test_HEXtoRGB_longerValue(self):
        """Test from HEX to RGB with string longer than 6 characters"""
        with pytest.raises(ValueError) as e:
            HEXtoRGB("#1b815ad")

    def test_HEXtoRGB_2_sharp(self):
        """Test from HEX to RGB with 2 # entered (i.e after a copy/paste)"""
        assert HEXtoRGB("##1b815a") == (27, 129, 90)
        
    def test_RGBtoANSI_background(self):
        assert RGBtoANSI("Test", (0, 10, 24), (255, 255, 255)) == f"\033[38;2;{0};{10};{24}m\033[48;2;{255};{255};{255}mTest\x1b[0m"
    
    def test_RGBtoANSI_background_list(self):
        assert RGBtoANSI("Test", [0, 10, 24], [255, 255, 255]) == f"\033[38;2;{0};{10};{24}m\033[48;2;{255};{255};{255}mTest\x1b[0m"

    def test_HEXtoANSI_valid_input(self):
        assert HEXtoANSI("Test HEX to ANSI", "#fdd374")
        
    def test_HEXtoANSI_no_foreground(self):
        with pytest.raises(ValueError) as e:
            HEXtoANSI("Text", "")
            