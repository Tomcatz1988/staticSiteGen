class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHtml(self):
        raise NotImplementedError("HTMLNode.toHtml has not been implemented")

    def propsToHtml(self):
        if self.props == None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string += f" {prop}=\"{self.props[prop]}\""
        return props_string

    def __repr__(self):
        return f"(HTMLNode)tag:\'{self.tag}\' / val:\'{self.value}\' / children:\'{self.children}\' / props:\'{self.props}\'" 


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def toHtml(self):
        if self.value == None:
            raise ValueError("leaf node has no value")
        html = ""
        match self.tag:        
            case None:
                html = f"{self.value}"
            case "img":
                html = f"<{self.tag}{self.propsToHtml()} />"
            case _:
                html = f"<{self.tag}{self.propsToHtml()}>{self.value}</{self.tag}>"
        return html


    def __repr__(self):
        return f"(HTMLNode)tag:\'{self.tag}\' / val:\'{self.value}\' / props:\'{self.props}\'" 


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def toHtml(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode has no children")
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.toHtml()
        html += f"</{self.tag}>"
        return html

