import unittest

from converter import JsonConverter
from utils import load_data


class TestUtils(unittest.TestCase):
    def test_load_data(self):
        data = [
            {
                "h3": "Title #1",
                "div": "Hello, World 1!"
            }
        ]
        loaded_data = load_data('source.json')
        self.assertEqual(loaded_data, data)


class TestConverterMethods(unittest.TestCase):

    def test_converter(self):
        data = [
            {
                "h3": "Title #1",
                "div": "Hello, World 1!"
            }
        ]
        html = '<h3>Title #1</h3><div>Hello, World 1!</div>'
        converter = JsonConverter(data)
        self.assertEqual(converter.convert(), html)

    def test_tags_cleaner(self):
        data = [
            {
                'h3': 'Title </h1><p>Other tag</p>',
                'div': 'Hello, World!</p>'
            }
        ]
        html = '<h3>Title Other tag</h3><div>Hello, World!</div>'
        converter = JsonConverter(data)
        converted_data = converter.convert()
        self.assertEqual(converted_data, html)


if __name__ == '__main__':
    unittest.main()
