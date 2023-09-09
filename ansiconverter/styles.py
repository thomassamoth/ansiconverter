from ansiconverter.converter import *

class Styles:
    """Apply different styles to the input text.

    Available:
        - bold
        - faint
        - italic
        - underline
        - bold & underline
        - strikethrough
        - reverse
    """

    RESET = "\x1b[0m"

    @staticmethod
    def bold(text):
        return f"\x1b[1m{text}{Styles.RESET}"

    @staticmethod
    def faint(text):
        return "\x1b[2m" + text + Styles.RESET

    @staticmethod
    def italic(text):
        return "\x1b[3m" + text + Styles.RESET

    @staticmethod
    def underline(text):
        return "\x1b[4m" + text + Styles.RESET

    @staticmethod
    def bold_and_underline(text):
        return "\x1b[1;4m" + text + Styles.RESET

    @staticmethod
    def strikethrough(text):
        return "\x1b[9m" + text + Styles.RESET

    @staticmethod
    def reverse(text):
        return "\x1b[7m" + text + Styles.RESET

