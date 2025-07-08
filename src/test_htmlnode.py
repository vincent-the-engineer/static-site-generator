import unittest

from htmlnode import HTMLNode


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
            {"class": "example"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(div, This is a test, children: None, {'class': 'example'})",
        )


if __name__ == "__main__":
    unittest.main()
