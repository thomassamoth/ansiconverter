import pytest

from ansiconverter import *

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
        assert HEXtoRGB("fef86c") == (254, 248, 108)
        assert bold(HEXtoANSI("Yellow", 'fef86c')) == '\x1b[1m\x1b[38;2;254;248;108mYellow\x1b[0m\x1b[0m'
        assert HEXtoANSI(bold("Yellow"), 'fef86c') == '\x1b[38;2;254;248;108m\x1b[1mYellow\x1b[0m\x1b[0m'
