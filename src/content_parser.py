from __future__ import annotations

import requests
from bs4 import BeautifulSoup

from tools import http_in_url_check


def parse_useful_content(url: str, parse_images: bool) -> str:
    """Parse useful site content by url."""

    url = http_in_url_check(url)

    try:
        page = requests.get(url)
    except requests.exceptions.MissingSchema:
        return 'INVALID URL'
    soup = BeautifulSoup(page.text, "html.parser")

    if parse_images:
        for img in soup.find_all('img'):
            img_url = img.attrs.get('src')
            if img_url.startswith('/'):
                # For url without 'http://'
                img_url = img_url[1:]
                img_url = url + img_url
            img.string = img_url

    useful_content = soup.get_text(' ', strip=True)
    return useful_content
