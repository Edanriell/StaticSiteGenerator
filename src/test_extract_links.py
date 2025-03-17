import unittest
from extract_links import extract_markdown_images, extract_markdown_links


class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        """Test extracting a single image."""
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_multiple(self):
        """Test extracting multiple images."""
        text = (
            "![rick roll](https://i.imgur.com/aKaOqIh.gif) and "
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_no_images(self):
        """Test when there are no images."""
        text = "This is text with no images."
        self.assertListEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links_single(self):
        """Test extracting a single link."""
        text = "This is a [link](https://www.boot.dev) to Boot.dev."
        expected = [("link", "https://www.boot.dev")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_multiple(self):
        """Test extracting multiple links."""
        text = (
            "Here is a [link1](https://www.example.com) and "
            "another [link2](https://www.google.com)"
        )
        expected = [
            ("link1", "https://www.example.com"),
            ("link2", "https://www.google.com"),
        ]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_no_links(self):
        """Test when there are no links."""
        text = "No links in this text."
        self.assertListEqual(extract_markdown_links(text), [])

    def test_ignore_image_links_in_link_extraction(self):
        """Test that image links are not extracted as regular links."""
        text = "![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertListEqual(extract_markdown_links(text), [])


if __name__ == "__main__":
    unittest.main()

