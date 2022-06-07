from __future__ import annotations

import sys

from content_parser import parse_useful_content
from tools import user_friendly_bool_arg_parse, break_line


def main(url: str,
         line_width: int = 80,
         parse_images: bool = False,
         save_to_file: bool = False) -> None:
    try:
        line_width = int(line_width)
    except TypeError:
        return print('Invalid type of line width, must be int')

    parse_images = user_friendly_bool_arg_parse(parse_images)
    save_to_file = user_friendly_bool_arg_parse(save_to_file)

    useful_content = parse_useful_content(url, parse_images)
    user_friendly_content = break_line(useful_content, line_width=line_width)

    if save_to_file:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(user_friendly_content)
    else:
        print(user_friendly_content)


if __name__ == '__main__':
    main(*sys.argv[1:])
