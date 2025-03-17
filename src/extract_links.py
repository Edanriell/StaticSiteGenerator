import re

def extract_markdown_images(text):
    """Extract markdown images from the text as (alt text, URL) tuples."""
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """Extract markdown links from the text as (anchor text, URL) tuples."""
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

