import unittest
from textnode import TextNode, TextType
from textToTextNode import textToTextNode


class testTextToTextNode(unittest.TestCase):
    def test_textToTestNode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = textToTextNode(text)
        self.assertEqual(text_nodes,
                        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_nested_textToTestNode(self):
        text = "This is **text** with **an _italic_** word and a `code block` and _an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and_** a [link](https://boot.dev)**"
        text_nodes = textToTextNode(text)
        self.assertEqual(text_nodes,
                        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("an ", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("an ", TextType.ITALIC),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and", TextType.ITALIC),
            TextNode(" a ", TextType.BOLD),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
