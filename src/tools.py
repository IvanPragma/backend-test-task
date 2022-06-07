from __future__ import annotations

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

    return textwrap.fill(text, width=line_width)


def http_in_url_check(url: str) -> str:
    """Check 'http://' in url and add it if does not exists."""

    if url.startswith('/'):
        url = url[1:]

    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url

    if not url.endswith('/'):
        url += '/'

    return url
