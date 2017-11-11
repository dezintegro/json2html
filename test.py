import unittest

from converter import JsonConverter
from utils import load_data


class TestUtils(unittest.TestCase):

    def test_load_data(self):
        data = [
            {
                "h3": "Title #1",
                "div": "Hello, World 1!"
            },
            {
                "h3": "Title #2",
                "div": "Hello, World 2!"
            }
        ]
        loaded_data = load_data('source.json')
        self.assertEqual(loaded_data, data)


class TestConverterMethods(unittest.TestCase):

    def test_list_converter(self):
        data = [
            {
                "h3": "Title #1",
                "div": "Hello, World 1!"
            },
            {
                "h3": "Title #2",
                "div": "Hello, World 2!"
            }
        ]
        html = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li>' \
               '<li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
        converter = JsonConverter(data)
        self.assertEqual(converter.convert(), html)

    def test_dict_converter(self):
        data = {
            "h3": "Title #1",
            "div": "Hello, World 1!"
        }
        html = '<h3>Title #1</h3><div>Hello, World 1!</div>'
        converter = JsonConverter(data)
        self.assertEqual(converter.convert(), html)

    def test_tags_cleaner(self):
        data = {
            'h3': 'Title </h1><p>Other tag</p>',
            'div': 'Hello, World!</p>'
        }
        clean_data = '<h3>Title Other tag</h3><div>Hello, World!</div>'
        unclean_data = '<h3>Title </h1><p>Other tag</p></h3>' \
                       '<div>Hello, World!</p></div>'

        converter = JsonConverter(data)
        converted_data = converter.convert()
        self.assertEqual(converted_data, clean_data)

        converter = JsonConverter(data, False)
        converted_data = converter.convert()
        self.assertEqual(converted_data, unclean_data)


if __name__ == '__main__':
    unittest.main()
