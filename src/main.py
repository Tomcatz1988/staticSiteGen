from textnode import *


def main():
    plain = TextNode("This is plain text", PLAIN_TEXT)
    bold = TextNode("Make this bold", BOLD_TEXT)
    italic = TextNode("This is italics", ITALIC_TEXT)
    code = TextNode("This should be code", CODE_TEXT)
    link = TextNode("Here is a link", LINK, "http://www.google.com")
    image = TextNode("Look at this picture", IMAGE, "http://www.imgur.com")
    print(f"{plain}'\n'{bold}'\n'{italic}'\n'{code}'\n'{link}'\n'{image}")
