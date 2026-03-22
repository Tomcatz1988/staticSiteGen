from textnode import TextNode, TextType


def splitNodesDelimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            temp_texts = node.text.split(delimiter, 2)
            match len(temp_texts):
                case 1:
                    new_nodes.append(node)
                case 3:
                    temp_nodes = []
                    temp_nodes.append(TextNode(temp_texts[0], TextType.TEXT))
                    temp_nodes.append(TextNode(temp_texts[1], text_type))
                    if temp_texts[2] != "":
                        temp_nodes.extend(splitNodesDelimiter( [TextNode(temp_texts[2], TextType.TEXT)], 
                                                              delimiter, 
                                                              text_type)
                        )
                    new_nodes.extend(temp_nodes)
                case _:
                    raise Exception(f"invalid markdown syntax - unmatched \'{delimiter}\' after {temp_texts[0].text[-30:]}")
        else:
            new_nodes.append(node)
    return new_nodes
