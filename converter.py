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
         to be rendered inside tag as values. Values may contain lists. In
         this case lists will be additionally wrapped in <ul> and <li> tags.

         Args:
             item (dict): Dict with tag names and values to convert

         Returns:
             list[str]: List of generated strings with markup.
        """
        result = []
        for tag, value in item.items():
            if type(value) == list:
                result.extend(self._convert_nested_tag(tag, value))
                return result
            if self.safe_convert:
                value = self.clear_tags(value)
            result.append(f'<{tag}>{value}</{tag}>')
        return result

    def _convert_nested_tag(self, tag, value):
        """Wraps in the tag nested list of elements

        Args:
            tag (str): The tag in which the elements will be wrapped.
            value (list): List of elements

        Returns:
            list: Result of converting `value` wrapped into `tag`

        """
        result = [f'<{tag}>']
        result.extend(self.convert(value))
        result.append(f'</{tag}>')
        return result

    def _convert_list(self, items):
        """Wraps list of elements in ul and li tags

        Args:
            items (list): List of elements which will be wrapped

        Returns:
            list: Result of converting `items` wrapped into ul and li tags

        """
        result = ['<ul>']
        for item in items:
            result.extend(self._convert_nested_tag('li', item))
        result.append('</ul>')
        return result

    def convert(self, items=None):
        """Converts `items` to HTML markup.

        Returns:
            str: Generated HTML markup.

        """
        if not items:
            items = self.items
        if type(items) == list:
            result = self._convert_list(items)
        else:
            result = self._convert_dict(items)
        return ''.join(result)
