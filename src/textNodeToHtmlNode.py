from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode


def textNodeToHtmlNode(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise Exception("cannot create HTMLNode <LINK> due to TextNode.url having None value")
            return LeafNode("a", text_node.text,
                            {"href": text_node.url}
            )
        case TextType.IMAGE:
            if text_node.url is None:
                raise Exception("cannot create HTMLNode <IMAGE> due to TextNode.url having None value")
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
                            } 
            )
        case _:
            raise Exception("cannot convert TextNode to HTMLNode due to invalid TextType")
