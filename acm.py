#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup

URL = sys.argv[1]

try:
    style = sys.argv[2].strip()
except:
    style = "sessions"


def get_full_link(link):
    return "/".join(URL.split("/")[:3]) + link


def get_paper_info(item):
    title = item.select("h5.issue-item__title")[0].string.split("\n")[0]
    title = title[:128].replace(" ", "_").replace("/", "")
    link = item.select('a[data-title="PDF"]')
    if link:
        return title, get_full_link(link[0]["href"])
    return None, None


def print_all_on_page(soup):
    for item in soup.select("div.issue-item-container"):
        name, link = get_paper_info(item)
        if name:
            print(f"{name} {link}")


page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")


if style == "simple":
    print_all_on_page(soup)


if style == "seemore":
    while True:
        print_all_on_page(soup)
        button = soup.select("div.proceedingsLazyLoad a")
        if not button:
            break
        page = requests.get(get_full_link(button[0]["href"]))
        soup = BeautifulSoup(page.text, "html.parser")


if style == "sessions":
    headingCount = len(soup.select("div.sections div.rlist div.toc__section"))
    for i in range(headingCount):
        sessionName = soup.select("a#heading" + str(i + 1))[0].string.lower()
        if "posters" in sessionName or "demos" in sessionName:
            continue
        page = requests.get(URL + "?tocHeading=heading" + str(i + 1))
        soup = BeautifulSoup(page.text, "html.parser")
        print_all_on_page(soup)
