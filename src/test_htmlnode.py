import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com",
                               "target": "_blank",})
        self.assertEqual(node.props_to_html(),
            'href="https://www.google.com" target="_blank"')

        node = HTMLNode(tag="<p>", value="text")
        self.assertEqual(node.props_to_html(), "")

        node = HTMLNode(value="test", props={"id":"value"})
        self.assertEqual(node.props_to_html(), 'id="value"')


    def test_values(self):
        node = HTMLNode(
            "p",
            "test text",
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_repr(self):
        node = HTMLNode(
            "div",
            "This is a test",
            None,
            {"class": "example",},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, This is a test, children: None, {'class': 'example'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode(
            tag="p",
            value="test text",
            props={"class": "myclass",},
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "myclass",})

#        with self.assertRaises(ValueError):
#            LeafNode(tag="div")

    def test_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()
