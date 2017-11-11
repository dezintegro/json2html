"""JSON data to HTML markup converter."""


import re


class JsonConverter:
    """
    Converts dicts in specified format to HTML markup.
    """

    def __init__(self, items, safe_convert=True):
        """Sets up text cleaning settings and initial state of `self.items`.

        Args:
            items (list[dict] or dict[str]): The list of dicts from which
                HTML markup will be generated. Dict must have tags names as
                keys and data which needs to be rendered inside tag as values.

            safe_convert (bool): Should or not value inside tag to be cleaned
                from tags.
        Raises:
            ValueError: If type of `items` not list or dict
        """
        if type(items) not in [list, dict]:
            raise ValueError('Items should be `list` or `dict` object.')
        self.items = items
        self.safe_convert = safe_convert
        self.tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

    def clear_tags(self, text):
        """Cleans the specified text from HTML tags.

        Args:
            text: Text which should to be cleaned from tags.

        Returns:
            str: Cleaned text.

        """
        return self.tag_re.sub('', text)

    def _convert_dict(self, item):
        """Converts dict to list of strings which contains HTML markup.

         Dict must have tags names as keys and data which needs
         to be rendered inside tag as values.

         Args:
             item (dict): Dict with tag names and values to convert

         Returns:
             list[str]: List of generated strings with markup.
        """

        result = []
        for tag, value in item.items():
            if self.safe_convert:
                value = self.clear_tags(value)
            result.append(f'<{tag}>{value}</{tag}>')
        return result

    def convert(self):
        """Converts dict or list of dicts in `self.items` to HTML markup.

        If type of `self.items` is list items will be wrapped into
        <ul> and <li> tags.

        Returns:
            str: Generated HTML markup.

        """

        if type(self.items) == list:
            result = ['<ul>']
            for item in self.items:
                result.append('<li>')
                result.extend(self._convert_dict(item))
                result.append('</li>')
            result.append('</ul>')
        else:
            result = self._convert_dict(self.items)
        return ''.join(result)
