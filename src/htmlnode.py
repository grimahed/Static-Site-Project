class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props:
            for prop in self.props:
                result += f' {prop}="{self.props[prop]}"'
        else:
            result = ""
        return result
    
    def __repr__(self):
        TAG = self.tag
        VALUE = self.value
        CHILDREN = self.children
        PROPS = self.props
        return f"{TAG}, {VALUE}, {CHILDREN}, {PROPS}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Cannot be valueless")
        if self.tag == None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}/>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        TAG = self.tag
        VALUE = self.value
        PROPS = self.props
        return f"{TAG}, {VALUE}, {PROPS}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None:
            raise ValueError("WHERE IS MY CHILD D:")
        child2 = ""
        for child in self.children:
            child2 += child.to_html()
        node_string = f"<{self.tag}{self.props_to_html()}>{child2}</{self.tag}>"
        return node_string
    
    def __repr__(self):
        TAG = self.tag
        CHILDREN = self.children
        PROPS = self.props
        return f"{TAG}, {CHILDREN}, {PROPS}"