"""Takes JSON data from `source.json` and convert it to HTML markup.

Example:
        $ python main.py
"""

from converter import JsonConverter
from utils import load_data


if __name__ == '__main__':
    data = load_data('source.json')
    converter = JsonConverter(data)
    html = converter.convert()
    print(html)
