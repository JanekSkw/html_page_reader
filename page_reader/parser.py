import logging
import re
from collections import Counter
from pathlib import Path

import requests

HTML_TAG_TOKEN = re.compile(r'(?:<.*?>)|(?:&#\d+?;)|(?:&quot;)', re.DOTALL)
EMPTY_CLEAN_TOKEN = re.compile(r'''[\s.;:,#{}()!@$?%*&/\\^"'\-_><+=\[\]]+''', re.DOTALL)
JS_CONTENT_TOKEN = re.compile(r'(?s)\s*<script\b.*?</script>', re.DOTALL)
CSS_CONTENT_TOKEN = re.compile(r'(?s)\s*<style\b.*?</style>', re.DOTALL)
logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


def get_url_content(url: str) -> str:
    """
    Connects to provided http url and acquire page content in string format
    :param url: string http address to acquire data
    :return: url response text content
    """
    response_data = requests.get(url)
    return response_data.text


def get_clean_text_from_html_content(text: str) -> str:
    """
    Clean raw html page text from css, javascript and html tags
    :param text: string with html content
    :return: clean text with removed all tags
    """
    """"""
    for token in [JS_CONTENT_TOKEN, CSS_CONTENT_TOKEN, HTML_TAG_TOKEN, EMPTY_CLEAN_TOKEN]:
        text = re.sub(token, ' ', text)
    logger.debug(f"Cleaned text:\n{text}")
    return text.strip()


def save_most_common_words_to_file(text: str, limit: int = 10, file_path: Path = Path('results.txt')):
    """
    Count N most common words that has occurred in text and write into the file `file_path`
    :param text: string text for searching most common words
    :param limit: integer value limiting amount of most common words aqquired from text
    :param file_path: path to file where most common words from text will be stored, default is `results.txt`
    """
    if text:
        words_counter = Counter(text.split(' '))
        most_common = words_counter.most_common(limit)
    else:
        most_common = [('EMPTY', 'TEXT')]
    with open(file_path, 'w') as results_file:
        results_file.write("\n".join('{} | {}'.format(k, v) for k, v in most_common))
        logger.info(f"Results successfully written to file: {file_path}")
