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
        return functools.reduce(lambda a: " " + str(a.keys()) + str(a.values()), self.props)