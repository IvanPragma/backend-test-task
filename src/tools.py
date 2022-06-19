from __future__ import annotations

import re
import textwrap
from typing import Union

yes_particles = 'yes yeah ye y да д true 1'.split()


def user_friendly_bool_arg_parse(value: Union[str, bool]) -> bool:
    """Simplifies user interaction.

    If value in yes_particles will return True,
    otherwise False.
    """

    return value if isinstance(value, bool) else value.lower() in yes_particles


def break_line(text: str, line_width: int = 80) -> str:
    """Break line by max line width."""

    # Remove double whitespaces
    while '  ' in text:
        text = text.replace('  ', ' ')

    lines = []
    current_line = ''
    current_line_len = 0
    for letter in text:
        if letter == '\n':
            if current_line:
                lines.append(current_line.strip())
            current_line = ''
            current_line_len = 0
            continue
        else:
            current_line += letter
        current_line_len += 1

        if current_line_len >= line_width:
            split_line = re.split('[ :;,\-.!)\n]', ''.join(reversed(current_line)), maxsplit=1)
            lines.append(''.join(reversed(split_line[-1])).strip())
            current_line = ''.join(reversed(split_line[0]))
            current_line_len = len(current_line)
    return '\n'.join(lines)


def http_in_url_check(url: str) -> str:
    """Check 'http://' in url and add it if does not exists."""

    if url.startswith('/'):
        url = url[1:]

    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url

    if not url.endswith('/'):
        url += '/'

    return url
