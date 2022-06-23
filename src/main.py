from __future__ import annotations

import sys

from content_parser import get_useful_content
from tools import user_friendly_bool_arg_parse


if __name__ == '__main__':
    server_mode = user_friendly_bool_arg_parse(sys.argv[1])
    if server_mode:
        from routes import app
        app.run(
            host='localhost',
            port=5000
        )
    else:
        is_file, result = get_useful_content(*sys.argv[2:])
        if is_file:
            print(f'Result was saved to output/{result}')
        else:
            print(result)
