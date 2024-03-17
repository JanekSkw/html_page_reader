import pytest
import responses

from page_reader.parser import get_clean_text_from_html_content, save_most_common_words_to_file, get_url_content
from.data.test_html_data import REF_HTML_1, REF_HTML_2, REF_HTML_3


@pytest.mark.parametrize("test_html_text, expected_results", [
    (REF_HTML_1, 'tytul | 5\nraz | 3\ndaw | 1\ntrzy | 1\njest | 1\nFajny | 1\ndwa | 1\na | 1\ng | 1\nh | 1'),
    (REF_HTML_2, 'a | 13\naa | 2\naaaa | 2\naaa | 1\naaaaaaa | 1'),
    (REF_HTML_3, 'EMPTY | TEXT'),
])
def test_parsing_text_is_ok(test_html_text, expected_results):
    clean_text = get_clean_text_from_html_content(test_html_text)
    save_most_common_words_to_file(clean_text)
    with open('results.txt') as results_file:
        test_results = results_file.read()

    assert test_results == expected_results


def test_parsing_real_page_is_ok():
    expected_results = 'the | 1185\nof | 907\nand | 634\nin | 553\nPoland | 509\nPolish | 273' \
                       '\na | 263\nThe | 253\nto | 199\nISBN | 180'
    with open('tests/data/ref_html_wiki_poland.txt') as test_html_file:
        test_html_text = test_html_file.read()

    clean_text = get_clean_text_from_html_content(test_html_text)
    save_most_common_words_to_file(clean_text)

    with open('results.txt') as results_file:
        test_results = results_file.read()
    assert test_results == expected_results


@responses.activate
def test_get_url_content():
    test_url = "https://en.wikipedia.org/wiki/Poland"
    with open('tests/data/ref_html_wiki_poland.txt') as test_html_file:
        ref_html_text = test_html_file.read()
    responses.add(responses.GET, test_url, body=ref_html_text, status=200)

    page_text = get_url_content(test_url)

    assert ref_html_text in page_text
