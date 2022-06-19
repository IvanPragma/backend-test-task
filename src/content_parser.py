from __future__ import annotations

import requests
from bs4 import BeautifulSoup
from readability import Document

from tools import http_in_url_check


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
