import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        
    def test_to_html_a(self):
        node = LeafNode("a", "Link", {"href": "https://example.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com">Link</a>',
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "What's up?")
        self.assertEqual(node.to_html(), "What's up?")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
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
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode(None, "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><b>child1</b>child2</div>")

    def test_to_html_with_children_props(self):
        child_node = LeafNode("a", "Click me!",
                              {"href": "https://www.google.com"})
        parent_node = ParentNode("body", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<body><a href="https://www.google.com">Click me!</a></body>'
        )


if __name__ == "__main__":
    unittest.main()
