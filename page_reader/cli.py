import click

from .parser import get_url_content, get_clean_text_from_html_content, save_most_common_words_to_file


@click.command()
@click.argument('page_url')
# @click.argument('limit', default=10)
@click.option('-v', '--verbose', is_flag=True)
def reader(page_url, verbose):
    """Program reads page content, removes html overhead, counts most common words and writes to file `results.txt`"""
    page_content = get_url_content(page_url)

    if verbose:
        with open('page_content.txt', 'w') as file_handler:
            file_handler.write(page_content)

    clean_text = get_clean_text_from_html_content(page_content)
    save_most_common_words_to_file(clean_text)
