from htmlnode import HTMLNode
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


if __name__ == "__main__":
    unittest.main()
