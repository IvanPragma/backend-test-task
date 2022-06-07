from __future__ import annotations

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

    return text
