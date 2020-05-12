#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup

URL = sys.argv[1]

try:
    style = sys.argv[2].strip()
except:
    style = "new"


def get_full_link(link):
    return "/".join(URL.split("/")[:3]) + link


page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
selector = "article.node-paper h2 a" if style == "new" else "div.node-paper h2 a"

for article in soup.select(selector):
    title = article.string
    if not title:
        continue
    title = title[:128].replace(" ", "_").replace("/", "")
    inner = requests.get(get_full_link(article["href"]))
    in_soup = BeautifulSoup(inner.text, "html.parser")
    link = in_soup.select("div.field-name-field-presentation-pdf span.file a")
    if link:
        print(f"{title} {link[-1]['href']}")
