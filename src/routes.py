from __future__ import annotations

from typing import Union

from flask import Flask, request, send_from_directory, Response

from content_parser import get_useful_content

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_route() -> Union[Response, dict]:
    """Main and only one route, that returns file."""

    url = request.args.get('url')
    line_width = request.args.get('line_width', 80)
    parse_images = request.args.get('parse_image', False)

    if not url:
        return {'success': False, 'detail': 'Request must content "url" attr'}

    is_file, result = get_useful_content(url=url,
                                         line_width=line_width,
                                         parse_images=parse_images,
                                         save_to_file=True)
    if is_file:
        return send_from_directory('output', result, as_attachment=True)
    else:
        return {'success': False, 'detail': result}
