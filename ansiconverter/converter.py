""" Convert any colour to the ANSI format to write in colours in your terminal.
Note: The conversion to an ANSI escape sequence may induce some colour variations. 
Also notice that some colours can't be mixed together as foreground and background.
"""


class Converter:
    """ANSI conversions and an additional function to convert RGB to HEX."""

    RESET = "\x1b[0m"

    #fmt: off
    @staticmethod
    def RGBtoANSI(text: str,foregound=(255, 255, 255),background=(),):
        """Write a text in RGB colour.

        Args:
            text (str): the text you want to write.
            foregound (tuple, optional): RGB foregound's colour. Defaults to (255, 255, 255).
            background (tuple, optional): RGB background's colour. Defaults to ().

        Raises:
            ValueError: the foregound colour can't be an empty list.

        Returns:
            string: the ANSI code for the foreground and the background.
        """
    #fmt: on
        if foregound != ():
            if background == ():
                return f"\033[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m{str(text)}{Converter.RESET}"
            else:
                return f"\033[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m\033[48;2;{background[0]};{background[1]};{background[2]}m{str(text)}{Converter.RESET}"
        else:
            raise ValueError(
                "The foregound can't be an empty list!\nNo paramaters will write the text in write"
            )

    @staticmethod
    def HEXtoRGB(fg="#000000"):
        """Convert a hexadecimal colour to its RGB triplet.

        Args:
            fg (str, optional): Hexadecimal colour value. Defaults to "#000000".

        Raises:
            ValueError: The colour is not a correct hexadecimal value.

        Returns:
            tuple: triplet of RGB values.
        """
        foreground = ""
        while True:
            foreground = fg.lstrip("#").lower()
            if len(foreground) == 6:
                return tuple(int(foreground[i : i + 2], base=16) for i in (0, 2, 4))

            else:
                raise ValueError("Enter a valid hexadecimal value")
                return 1

    @staticmethod
    def HEXtoANSI(text, foreground="#ffffff", background=""):
        from ansiconverter import HEXtoRGB, RGBtoANSI

        foregroundRGB = HEXtoRGB(foreground)
        if foreground != "":
            if background != "":
                backgroundRGB = HEXtoRGB(background)
                return RGBtoANSI(text, foregroundRGB, backgroundRGB)
            else:
                return RGBtoANSI(text, foregroundRGB)

        else:
            raise ValueError("Please enter at least one foreground colour.")

    @staticmethod
    # Utility to convert to other colour format
    def RGBtoHEX(rgb=(255, 255, 255)):
        if rgb != ():
            return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        else:
            raise ValueError(f"The colour can't be empty. Please retry.")
