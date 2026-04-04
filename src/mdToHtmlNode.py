from blocktype import BlockType, blockToBlockType
from htmlnode import LeafNode, ParentNode
from mdToBlocks import mdToBlocks
from textnode import TextType, TextNode
from textToTextNode import textToTextNode
from textNodeToHtmlNode import textNodeToHtmlNode


def mdToHtmlNode(md):
    mdBlocks = mdToBlocks(md)
    htmlChildren = []
    for block in mdBlocks:
        match blockToBlockType(block):
            case BlockType.PARAGRAPH:
                htmlChildren.append(mdToHtmlParagraph(block))
            case BlockType.HEADING:
                htmlChildren.append(mdToHtmlHeading(block))
            case BlockType.CODE:
                htmlChildren.append(mdToHtmlCode(block))
            case BlockType.QUOTE:
                htmlChildren.append(mdToHtmlQuote(block))
            case BlockType.UO_LIST:
                htmlChildren.append(mdToHtmlUOList(block))
            case BlockType.ORD_LIST:
                htmlChildren.append(mdToHtmlOrdList(block))
    return ParentNode("div", htmlChildren)


def textNodeToHtmlNodeList(textNodeList):
    htmlChildren = []
    for node in textNodeList:
        htmlChildren.append(textNodeToHtmlNode(node))
    return htmlChildren


def mdToHtmlParagraph(block):
    lines = block.split("\n")
    text = " ".join(lines)
    textNodes = textToTextNode(text)
    return ParentNode('p', textNodeToHtmlNodeList(textNodes))


def mdToHtmlHeading(block):
    splitBlock = block.split(" ", maxsplit=1)
    mdTag =  splitBlock[0]
    headingText = splitBlock[1]
    headingDepth = len(mdTag)
    htmlTag = f"h{headingDepth}"
    textNodes = textToTextNode(headingText)
    return ParentNode(htmlTag, textNodeToHtmlNodeList(textNodes))


def mdToHtmlCode(block):
    splitBlock = block.split("```")
    codeBlock = splitBlock[1][1:]   # the first and third elements are empty strings from the split
                                    # and slice off the first char to get rid of new line
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, codeBlock)])])


def mdToHtmlQuote(block):
    lineList = block.split(">")
    fullQuote = ""
    for line in lineList:
        fullQuote = fullQuote + line.strip() + " "
    textNodes = textToTextNode(fullQuote.strip())
    return ParentNode("blockquote", textNodeToHtmlNodeList(textNodes))


def mdToHtmlUOList(block):
    lines = block.split("\n")
    listElements = []
    for line in lines:
        tmpLine = line.lstrip("- ")
        textNodes = textToTextNode(tmpLine)
        listElements.append(ParentNode("li", textNodeToHtmlNodeList(textNodes)))
    return ParentNode("ul", listElements)


def mdToHtmlOrdList(block):
    lines = block.split("\n")
    listElements = []
    for line in lines:
        sepLeaderAndText = line.split(" ", maxsplit=1)
        textNodes = textToTextNode(sepLeaderAndText[1].strip())
        listElements.append(ParentNode("li", textNodeToHtmlNodeList(textNodes)))
    return ParentNode("ol", listElements)
