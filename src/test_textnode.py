import unittest

from htmlnode import LeafNode
from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)


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
        node2 = TextNode("This is a text node", TextType.TEXT)
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


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("BOLD TEST", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "BOLD TEST")

    def test_italic(self):
        node = TextNode("italic test", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic test")

    def test_code(self):
        node = TextNode('print("Hello world!")', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 'print("Hello world!")')

    def test_link(self):
        node = TextNode("my link", TextType.LINK, "https://example.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "my link")
        self.assertEqual(html_node.props.get("href"), "https://example.org")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props.get("src"), "https://example.com")
        self.assertEqual(html_node.props.get("alt"), "alt text")


if __name__ == "__main__":
    unittest.main()
