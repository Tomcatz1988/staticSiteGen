import unittest
from splitnodes import splitNodesDelimiter
from textnode import TextNode, TextType
from delimiter_map import inline_delimiter_map


class testSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "`")
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_bold_split(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "**")
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_italic_split(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "_")
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_code_split_short(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "`")
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ]
        )

    def test_multipe_code_splits(self):
        node = TextNode("This is text with multiple `code block` words `this is a test`", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "`")
        self.assertEqual(new_nodes, [
                TextNode("This is text with multiple ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" words ", TextType.TEXT),
                TextNode("this is a test", TextType.CODE),
            ]
        )

    def test_different_delimiter_splits(self):
        node = TextNode("This is text with multiple `code block` words _this is a test_", TextType.TEXT)
        new_nodes = splitNodesDelimiter([node], "`")
        new_nodes = splitNodesDelimiter(new_nodes, "_")
        self.assertEqual(new_nodes, [
                TextNode("This is text with multiple ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" words ", TextType.TEXT),
                TextNode("this is a test", TextType.ITALIC),
            ]
        )
    def test_nested_delimiter_splits(self):
        node = TextNode("This is text with **multiple `code block`** words _this `is a` test_", TextType.TEXT)
        new_nodes = [node]
        for delimiter in inline_delimiter_map:
            new_nodes = splitNodesDelimiter(new_nodes, delimiter)
        self.assertEqual(new_nodes, [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("multiple ", TextType.BOLD),
                TextNode("code block", TextType.CODE),
                TextNode(" words ", TextType.TEXT),
                TextNode("this ", TextType.ITALIC),
                TextNode("is a", TextType.CODE),
                TextNode(" test", TextType.ITALIC)
            ]
        )
