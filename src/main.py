from textnode import *


def main():
    plain = TextNode("This is plain text", TextType.PLAIN)
    bold = TextNode("Make this bold", TextType.BOLD)
    italic = TextNode("This is italics", TextType.ITALIC)
    code = TextNode("This should be code", TextType.CODE)
    link = TextNode("Here is a link", TextType.LINK, "http://www.google.com")
    image = TextNode("Look at this picture", TextType.IMAGE, "http://www.imgur.com")
    print(f"{plain}\n{bold}\n{italic}\n{code}\n{link}\n{image}")

if __name__ == "__main__":
    main()
