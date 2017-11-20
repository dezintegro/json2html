import unittest

from converter import JsonConverter
from utils import load_data


class TestUtils(unittest.TestCase):

    def test_load_data(self):
        data = [
            {
                "span": "Title #1",
                "content": [
                    {
                        "p": "Example 1",
                        "header": "header 1"
                    }
                ]
            },
            {"div": "div 1"}
        ]
        loaded_data = load_data('source.json')
        self.assertEqual(data, loaded_data)


class TestConverterMethods(unittest.TestCase):

    def test_list_converter(self):
        data = [
            {
                "span": "Title #1",
                "content": [
                    {
                        "p": "Example 1",
                        "header": "header 1"
                    }
                ]
            },
            {"div": "div 1"}
        ]
        html = '<ul><li><span>Title #1</span><content><ul><li>' \
               '<p>Example 1</p><header>header 1</header></li>' \
               '</ul></content></li><li><div>div 1</div></li></ul>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

    def test_dict_converter(self):
        data = {
            "h3": "Title #1",
            "div": "Hello, World 1!"
        }
        html = '<h3>Title #1</h3><div>Hello, World 1!</div>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

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
        self.assertEqual(clean_data, converted_data)

        converter = JsonConverter(data, False)
        converted_data = converter.convert()
        self.assertEqual(unclean_data, converted_data)


if __name__ == '__main__':
    unittest.main()
