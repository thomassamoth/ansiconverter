from .converter import Converter
from .styles import Styles

# Export the Styles class and styling functions
bold = Styles().bold
faint = Styles().faint
italic = Styles().italic
underline = Styles().underline
bold_and_underline = Styles().bold_and_underline
strikethrough = Styles().strikethrough
reverse = Styles().reverse

# Export the Converter methods
RGBtoANSI = Converter().RGBtoANSI
RGBtoHEX = Converter().RGBtoHEX
HEXtoANSI = Converter().HEXtoANSI
HEXtoRGB = Converter().HEXtoRGB

# Are imported whrn writing from ansiconverter import *
__all__ = ['Styles', 'bold', 'faint', 'italic', 'underline', 'bold_and_underline', 'strikethrough', 'reverse',]

__all__.extend(['RGBtoANSI', 'RGBtoHEX', 'HEXtoANSI', 'HEXtoRGB'])