from ansiconverter.converter import *


class styles:
    """Apply different styles to the input text.

    Available :
        - bold
        - faint
        - italic
        - underline
        - bold & underline
        - strikethrough
        - reverse
    """

    RESET = "\x1b[0m"

    def bold(text):
        return f"\033[1m{text}{styles.RESET}"

    def faint(text):
        return "\033[2m" + text + styles.RESET

    def italic(text):
        return "\033[3m" + text + styles.RESET

    def underline(text):
        return "\033[4m" + text + styles.RESET

    def bold_and_underline(text):
        return "\033[1;4m" + value + styles.RESET

    def strikethrough(text):
        return "\033[9m" + text + styles.RESET

    def reverse(text):
        return "\033[7m" + text + styles.RESET


class bootstrap_inspired:
    pass
