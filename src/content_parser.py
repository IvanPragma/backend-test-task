from __future__ import annotations

import random

import requests
from bs4 import BeautifulSoup
from readability import Document

from tools import http_in_url_check, user_friendly_bool_arg_parse, break_line


def parse_useful_content(url: str, parse_images: bool) -> str:
    """Parse useful site content by url."""

    url = http_in_url_check(url)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'
        }
        page = requests.get(url, headers=headers)
    except requests.exceptions.MissingSchema:
        return 'INVALID URL'
    except requests.exceptions.ConnectionError:
        return 'CONNECTION ERROR'

    doc = Document(page.text,
                   min_text_length=20)
    soup = BeautifulSoup(doc.summary(), "html.parser")

    if parse_images:
        for img in soup.find_all('img'):
            img_url = img.attrs.get('src')
            if img_url.startswith('/'):
                # For url without 'http://'
                img_url = img_url[1:]
                img_url = url + img_url
            img.string = img_url

    for br in soup.find_all('br'):
        br.string = '\n'

    useful_content = soup.get_text(' ')
    return useful_content


def get_useful_content(url: str,
                       line_width: int = 80,
                       parse_images: bool = False,
                       save_to_file: bool = False) -> tuple[bool, str]:
    """Return tuple of is_file (bool) and useful content, wrapped by line width, or file path."""

    try:
        line_width = int(line_width)
    except TypeError:
        return False, 'Invalid type of line width, must be int'

    parse_images = user_friendly_bool_arg_parse(parse_images)
    save_to_file = user_friendly_bool_arg_parse(save_to_file)

    useful_content = parse_useful_content(url, parse_images)
    user_friendly_content = break_line(useful_content, line_width=line_width)

    if save_to_file:
        path = f'{random.randint(0, 9999)}.txt'
        with open('output/' + path, 'w', encoding='utf-8') as f:
            f.write(user_friendly_content)
        return True, path
    else:
        return False, user_friendly_content
