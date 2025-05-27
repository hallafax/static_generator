import functools

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self,other):
       return self.tag == other.tag and self.value == other.value and self.children == other.children  and self.props == other.props
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, child: {self.children}, attribute: {self.props}"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        for key in self.props:
            prop_string += f' {key}="{self.props[key]}"'
        return prop_string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag,value,None,props)
        if children!=None:
            raise Exception("cannot have children")

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return str(self.value)
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:    
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

