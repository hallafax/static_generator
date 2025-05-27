from htmlnode import HTMLNode, LeafNode
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
        node2 = LeafNode("a", "Click me!", None, {"href": "https://www.google.com", })
        node3 = LeafNode("a", "Click me!", None, {"href": "https://www.google.com", "color": "red" })
        node4 = LeafNode("b", None)

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com" color="red">Click me!</a>')
        with self.assertRaises(ValueError):
            node4.to_html()
        with self.assertRaises(Exception):
            node5= LeafNode("p", "this is hard", "b", {"color": "red"})


if __name__ == "__main__":
    unittest.main()
