import re
from textnode import TextNode, TextType
from constants import INLINE_DELIMITER_MAP, INLINE_TEXT_TYPE


def textToTextNode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    for delimiter in INLINE_DELIMITER_MAP:
        nodes = splitNodesDelimiter(nodes, delimiter)
    nodes = splitNodesEmbedded(nodes, TextType.LINK)
    nodes = splitNodesEmbedded(nodes, TextType.IMAGE)
    return nodes


def splitNodesDelimiter(old_nodes, delimiter):
    new_nodes = []
    for node in old_nodes:
        if node.text_type in INLINE_TEXT_TYPE:
            temp_texts = node.text.split(delimiter, 2)
            match len(temp_texts):
                case 1:
                    new_nodes.append(node)
                case 3:
                    temp_nodes = []
                    temp_nodes.append(TextNode(temp_texts[0], node.text_type))
                    temp_nodes.append(TextNode(temp_texts[1], INLINE_DELIMITER_MAP[delimiter]))
                    if temp_texts[2] != "":
                        temp_nodes.extend(splitNodesDelimiter( [TextNode(temp_texts[2], node.text_type)], delimiter) )
                    new_nodes.extend(temp_nodes)
                case _:
                    raise Exception(f"invalid markdown syntax - unmatched \'{delimiter}\' after \'{temp_texts[0].text[-30:]}\'")
        else:
            new_nodes.append(node)
    return new_nodes


def splitNodesEmbedded(old_nodes, text_type):
    if ((text_type != TextType.LINK) and (text_type != TextType.IMAGE)):
        return old_nodes
    new_nodes = []
    for node in old_nodes:
        links = extractMarkdownLinks(node.text) if text_type == TextType.LINK else extractMarkdownImages(node.text)
        if ((node.text_type in INLINE_TEXT_TYPE) and (len(links) > 0)):
            if len(links) > 0:
                delimiter = f"[{links[0][0]}]({links[0][1]})" if text_type == TextType.LINK else f"![{links[0][0]}]({links[0][1]})"
                texts = node.text.split(delimiter)
                temp_nodes= []
                for i in range(len(texts)):
                    if texts[i] != "":
                        temp_nodes.append(TextNode(texts[i], node.text_type))
                    if (i < (len(texts) - 1)):
                        link_node = TextNode(links[0][0], text_type, url=links[0][1])
                        temp_nodes.append(link_node)
                if len(links) > 1:
                    new_nodes.extend(splitNodesEmbedded(temp_nodes, text_type))
                else:
                    new_nodes.extend(temp_nodes)
        else:
            new_nodes.append(node)
    return new_nodes


def extractMarkdownImages(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extractMarkdownLinks(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
