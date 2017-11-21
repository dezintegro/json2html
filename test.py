import unittest

from converter import JsonConverter
from utils import load_data


class TestUtils(unittest.TestCase):

    def test_load_data(self):
        data = {
            "p.my-class#my-id": "hello",
            "p.my-class1.my-class2": "example<a>asd</a>"
        }
        loaded_data = load_data('source.json')
        self.assertEqual(data, loaded_data)


class TestConverterMethods(unittest.TestCase):

    def test_list_converter(self):
        data = [
            {
                "span": "Title #1",
                "content": [
                    {
                        "p.test#test": "Example 1",
                        "header": "header 1"
                    }
                ]
            },
            {"div.test#test-1": "div 1"}
        ]
        html = '<ul><li><span>Title #1</span><content><ul><li>' \
               '<p id="test" class="test">Example 1</p><header>header ' \
               '1</header></li></ul></content></li><li><div id="test-1"' \
               ' class="test">div 1</div></li></ul>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

    def test_dict_converter(self):
        data = {
            "p": "hello",
            "div": "example"
        }
        html = '<p>hello</p><div>example</div>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

    def test_styled_dict_converter(self):
        data = {
            "p.my-class#my-id": "hello",
            "p.my-class1.my-class2": "example<a>asd</a>"
        }
        html = '<p id="my-id" class="my-class">hello</p><p ' \
               'class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

    def test_style_positions(self):
        data_class_first = {
            "p.my-class#my-id": "hello",
            "p.my-class1.my-class2": "example<a>asd</a>"
        }
        data_id_first = {
            "p#my-id.my-class": "hello",
            "p.my-class1.my-class2": "example<a>asd</a>"
        }
        html = '<p id="my-id" class="my-class">hello</p><p ' \
               'class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>'
        converter = JsonConverter(data_class_first)
        self.assertEqual(html, converter.convert())

        converter = JsonConverter(data_id_first)
        self.assertEqual(html, converter.convert())

    def test_invalid_style_converter(self):
        """Tests extracting data from invalid styles.

        """
        data = {
            "p...my-class#.my-id": "hello",
            "p.#my-class1...my-class2": "example<a>asd</a>"
        }
        html = '<p class="my-class my-id">hello</p><p ' \
               'id="my-class1" class="my-class2">example&lt;a&gt;asd&' \
               'lt;/a&gt;</p>'
        converter = JsonConverter(data)
        self.assertEqual(html, converter.convert())

    def test_tags_cleaner(self):
        data = {
            "p": "hello",
            "div": "example<a>asd</a>"
        }
        clean_data = '<p>hello</p><div>example&lt;a&gt;' \
                     'asd&lt;/a&gt;</div>'

        unclean_data = '<p>hello</p><div>example<a>asd</a></div>'

        converter = JsonConverter(data)
        converted_data = converter.convert()
        self.assertEqual(clean_data, converted_data)

        converter = JsonConverter(data, False)
        converted_data = converter.convert()
        self.assertEqual(unclean_data, converted_data)


if __name__ == '__main__':
    unittest.main()
