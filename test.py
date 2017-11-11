import unittest

from converter import JsonConverter
from utils import load_data


class TestUtils(unittest.TestCase):
    def test_load_data(self):
        data = [
            {
                "title": "Title #1",
                "body": "Hello, World 1!"
            },
            {
                "title": "Title #2",
                "body": "Hello, World 2!"
            }
        ]
        loaded_data = load_data('source.json')
        self.assertEqual(loaded_data, data)


class TestConverterMethods(unittest.TestCase):

    def test_converter(self):
        data = [
            {
                "title": "Title #1",
                "body": "Hello, World 1!"
            },
            {
                "title": "Title #2",
                "body": "Hello, World 2!"
            }
        ]
        html = '<h1>Title #1</h1><p>Hello, World 1!</p>' \
               '<h1>Title #2</h1><p>Hello, World 2!</p>'
        converter = JsonConverter(data)
        self.assertEqual(converter.convert(), html)

    def test_tags_cleaner(self):
        data = [
            {
                'title': 'Title </h1><p>Other tag</p>',
                'body': 'Hello, World!</p>'
            }
        ]
        html = '<h1>Title Other tag</h1><p>Hello, World!</p>'
        converter = JsonConverter(data)
        converted_data = converter.convert()
        self.assertEqual(converted_data, html)


if __name__ == '__main__':
    unittest.main()
