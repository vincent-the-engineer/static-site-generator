import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node too", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("THIS IS A TEXT NODE", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

        node = TextNode("My link", TextType.LINK, "https://example.org")
        node2 = TextNode("My link", TextType.LINK, "https://example.org")
        self.assertEqual(node, node2)

        node = TextNode("My link 1", TextType.LINK, "https://example.org")
        node2 = TextNode("My link 2", TextType.LINK, "https://example.org")
        self.assertNotEqual(node, node2)

        node = TextNode("My link", TextType.LINK, "https://example.org")
        node2 = TextNode("My link", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)

        node = TextNode("My link", TextType.LINK, "https://example.org")
        node2 = TextNode("My link", TextType.LINK)
        self.assertNotEqual(node, node2)


    def test_repr(self):
            node = TextNode("test test", TextType.LINK, "https://example.org")
            self.assertEqual(node.__repr__(),
                "TextNode(test test, link, https://example.org)")


if __name__ == "__main__":
    unittest.main()
