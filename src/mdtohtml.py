from blocktype import BlockType, blockToBlockType
from htmlnode import LeafNode, ParentNode
from textnode import TextType, TextNode
from texttonode import textToTextNode
from texttohtml import textNodeToHtmlNode


def mdToHtmlNode(md):
    md_blocks = mdToBlocks(md)
    html_children = []
    for block in md_blocks:
        match blockToBlockType(block):
            case BlockType.PARAGRAPH:
                html_children.append(mdToHtmlParagraph(block))
            case BlockType.HEADING:
                html_children.append(mdToHtmlHeading(block))
            case BlockType.CODE:
                html_children.append(mdToHtmlCode(block))
            case BlockType.QUOTE:
                html_children.append(mdToHtmlQuote(block))
            case BlockType.UO_LIST:
                html_children.append(mdToHtmlUOList(block))
            case BlockType.ORD_LIST:
                html_children.append(mdToHtmlOrdList(block))
    return ParentNode("div", html_children)


def mdToBlocks(md):
    blocks = md.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        tmp_block = block.strip()
        if tmp_block != "":
            stripped_blocks.append(tmp_block)
    return stripped_blocks


def textToHtmlNodeList(text):
    text_nodes = textToTextNode(text)
    html_children = []
    for node in text_nodes:
        html_children.append(textNodeToHtmlNode(node))
    return html_children


def mdToHtmlParagraph(block):
    lines = block.split("\n")
    text = " ".join(lines)
    return ParentNode('p', textToHtmlNodeList(text))


def mdToHtmlHeading(block):
    split_block = block.split(" ", maxsplit=1)
    md_tag =  split_block[0]
    heading_text = split_block[1]
    heading_depth = len(md_tag)
    html_tag = f"h{heading_depth}"
    return ParentNode(html_tag, textToHtmlNodeList(heading_text))


def mdToHtmlCode(block):
    split_block = block.split("```")
    code_block = split_block[1][1:]   # the first and third elements are empty strings from the split
                                    # and slice off the first char to get rid of new line
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, code_block)])])


def mdToHtmlQuote(block):
    lines = block.split(">")
    full_quote = ""
    for line in lines:
        full_quote = full_quote + line.strip() + " "
    return ParentNode("blockquote", textToHtmlNodeList(full_quote.strip()))


def mdToHtmlUOList(block):
    lines = block.split("\n")
    list_elemets = []
    for line in lines:
        tmp_line = line.lstrip("- ")
        list_elemets.append(ParentNode("li", textToHtmlNodeList(tmp_line)))
    return ParentNode("ul", list_elemets)


def mdToHtmlOrdList(block):
    lines = block.split("\n")
    list_elemets = []
    for line in lines:
        sep_leader_and_text = line.split(" ", maxsplit=1)
        text = sep_leader_and_text[1].strip()
        list_elemets.append(ParentNode("li", textToHtmlNodeList(text)))
    return ParentNode("ol", list_elemets)
