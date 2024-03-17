
## Install

>ppip install .

## Usage
>page-reader --help

Usage: page-reader [OPTIONS] PAGE_URL

  Program reads page content, removes html overhead, counts most common words
  and writes to file `results.txt`

Options:
  -v, --verbose
  --help         Show this message and exit.

## Test coverage
>pip install pytest coverage responses

>coverage html && open htmlcov/index.html



