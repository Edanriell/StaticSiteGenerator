class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        """This method should be implemented by child classes."""
        raise NotImplementedError("to_html method must be implemented by child classes")

    def props_to_html(self):
        """Convert props to HTML string format."""
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        """Return a string representation for debugging purposes."""
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        # No children allowed for LeafNode
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        """Render the leaf node as an HTML string."""
        if self.value is None:
            raise ValueError("LeafNode must have a value.")

        # If no tag, return raw text
        if self.tag is None:
            return self.value

        # Render HTML tag with props if any
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if children is None or not isinstance(children, list):
            raise ValueError("ParentNode must have children as a list.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """Render the parent node and all its children recursively."""
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")

        # Convert children to HTML recursively
        children_html = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
