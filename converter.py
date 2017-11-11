"""JSON data to HTML markup converter."""


import re


class JsonConverter:
    """
    Converts dicts in specified format to HTML markup.
    """

    def __init__(self, items):
        """Sets up regexp for cleaning text and initial state of `self.items`.

        Args:
            items (list[dict]): The list of dicts from which
                HTML markup will be generated.
        """
        self.items = items
        self.tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

    def clear_tags(self, text):
        """Cleans the specified text from HTML tags.

        Args:
            text: Text which should to be cleaned from tags.

        Returns:
            str: Cleaned text.

        """
        return self.tag_re.sub('', text)

    def convert(self, clear_tags=True):
        """Converts list of dicts to HTML markup.

        Dicts in list must have tags names as keys and data which needs
        to be rendered inside tag as values.

        Args:
            clear_tags (bool): Should or not value inside tag to be cleaned
            from tags.

        Returns:
            str: Generated HTML markup.

        """

        result = []
        for item in self.items:
            for tag, value in item.items():
                if clear_tags:
                    value = self.clear_tags(value)
                result.append(f'<{tag}>{value}</{tag}>')
        return ''.join(result)
