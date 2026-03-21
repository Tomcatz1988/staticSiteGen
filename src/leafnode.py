from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node has no value")
        match self.tag:        
            case None:
                return f"{value}"
            case "img":
                return f"<{self.tag}{self.props_to_html()} />"
            case _:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"(HTMLNode)tag:\'{self.tag}\' / val:\'{self.value}\' / props:\'{self.props}\'" 
