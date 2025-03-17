import unittest
from htmlnode import ParentNode, LeafNode, HTMLNode


class TestHTMLNode(unittest.TestCase):
    
    def test_empty_node(self):
        """Test that an empty node initializes correctly."""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html_empty(self):
        """Test that an empty props dictionary returns an empty string."""
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        """Test single property conversion."""
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        """Test multiple properties conversion."""
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        """Test the __repr__ method."""
        node = HTMLNode("a", "Click here", [], {"href": "https://www.example.com"})
        expected_repr = "HTMLNode(tag=a, value=Click here, children=[], props={'href': 'https://www.example.com'})"
        self.assertEqual(repr(node), expected_repr)


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        """Test a simple <p> tag."""
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        """Test a leaf node with properties."""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_tag_returns_raw_text(self):
        """Test that a node with no tag returns raw text."""
        node = LeafNode(None, "Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")

    def test_leaf_no_value_raises_error(self):
        """Test that a missing value raises a ValueError."""
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_no_children_allowed(self):
        """Test that children cannot be passed to a LeafNode."""
        node = LeafNode("p", "No children allowed")
        self.assertEqual(node.children, [])  # LeafNode should have no children

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        """Test rendering a parent node with one child."""
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        """Test rendering a parent node with nested children."""
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_tag_raises_error(self):
        """Test that missing tag raises ValueError."""
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")])

    def test_no_children_raises_error(self):
        """Test that missing children raises ValueError."""
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_to_html_multiple_children(self):
        """Test rendering multiple children."""
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_node_with_props(self):
        """Test parent node with props."""
        node = ParentNode("div", [LeafNode("span", "child")], {"class": "container"})
        self.assertEqual(
            node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

if __name__ == "__main__":
    unittest.main()
