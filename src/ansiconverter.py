""" Convert any color to the ANSI format to write in colors in your terminal."""

RESET = "\x1b[0m"


class converter:
    """ANSI conversions and an additional function to convert RGB to HEX."""

    RESET = "\x1b[0m"

    def RGBtoANSI(foregound=[255, 255, 255], background=[]):
        """Convert a RGB color to ANSI code.

        Args:
            foregound (list, optional): text's color. Defaults to [255, 255, 255] = white.
            background (list, optional): background's color to highlight the text. Defaults to [].

        Raises:
            ValueError: the foregound color can't be an empty list

        Returns:
            string: the ANSI codes for the foregound and background colors.
        """
        if foregound != []:
            if background == []:
                return f"\x1B[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m"
            else:
                return f"\x1B[38;2;{foregound[0]};{foregound[1]};{foregound[2]}m\x1B[48;2;{background[0]};{background[1]};{background[2]}m"
        else:
            raise ValueError(
                "The foregound can't be an empty list!\nNo paramaters will write the text in write"
            )

    def HEXtoRGB(fg="#000000"):
        """Convert a hexadecimal color to its RGB triplet.

        Args:
            fg (str, optional): Hexadecimal color value. Defaults to "#000000".

        Raises:
            ValueError: The color is not a correct hexadecimal value.

        Returns:
            list: triplet of RGB values.
        """
        foreground = ""
        while True:
            foreground = fg.lstrip("#").lower()
            if len(foreground) == 6:
                return list(int(foreground[i : i + 2], base=16) for i in (0, 2, 4))

            else:
                raise ValueError("Enter a valid hexadecimal value")
                return 1

    def HEXtoANSI(hex_color):
        RGB_list = converter.HEXtoRGB(hex_color)
        return converter.RGBtoANSI(RGB_list)

    # Utility to convert to other color format

    def RGBtoHEX(rgb=[255, 255, 255]):
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


class basics:
    fgBlack = converter.HEXtoANSI("#000000")
    fgWhite = converter.HEXtoANSI("#ffffff")

    bgBlack = "\x1B[40m"
    bgWhite = "\x1B[47m"


class styles:
    """Apply different styles to the input text."""

    RESET = "\x1b[0m"

    def bold(text):
        return "\033[1m" + text + RESET

    def faint(text):
        return "\033[2m" + text + RESET

    def italic(text):
        return "\033[3m" + text + RESET

    def underline(text):
        return "\033[4m" + text + RESET

    def bold_and_underline(text):
        return "\033[1;4m" + value + RESET

    def strikethrough(text):
        return "\033[9m" + text + RESET

    def reverse(text):
        return "\033[7m" + text + RESET


class bootstrap_inpired:
    pass
