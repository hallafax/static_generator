from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "all is well")
        node2 = HTMLNode("p", "all is well")
        node3 = HTMLNode("p", "all is well", [node,node2], {"href": "https://www.google.com"})
        node4 = HTMLNode("p", "all is well", [node,node2], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com", })
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "color": "red" })
        node4 = LeafNode("b", None)

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com" color="red">Click me!</a>')
        with self.assertRaises(ValueError):
            node4.to_html()
        with self.assertRaises(Exception):
            node5= LeafNode("p", "this is hard", "b", {"color": "red"})

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(child_node.to_html(), "<span>child</span>")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        child4 = LeafNode(None, "Normal text")
        parent = ParentNode("p", [child1, child2, child3, child4])
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    def test_to_html_with_complex_gerations(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        child4 = LeafNode(None, "Normal text")
        parent1 = ParentNode("span", [child1, child2])
        parent2 = ParentNode("span", [child3, child4])
        grandparent = ParentNode("p", [parent1, parent2])
        self.assertEqual(
            grandparent.to_html(),
            "<p><span><b>Bold text</b>Normal text</span><span><i>italic text</i>Normal text</span></p>"
        )

if __name__ == "__main__":
    unittest.main()
