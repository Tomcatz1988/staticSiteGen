from delimiter_map import inline_delimiter_map
from splitnodes import splitNodesDelimiter, splitNodesEmbedded
from textnode import TextNode, TextType


def textToTextNode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    for delimiter in inline_delimiter_map:
        nodes = splitNodesDelimiter(nodes, delimiter)
    nodes = splitNodesEmbedded(nodes, TextType.LINK)
    nodes = splitNodesEmbedded(nodes, TextType.IMAGE)
    return nodes

