# -*- coding: utf-8 -*-

import os
import re

import click
import crayons
import requests
from bs4 import BeautifulSoup

# Make fzf with a big list of norwegian words
# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
# https://stackoverflow.com/questions/27114942/exclude-hidden-tags-while-scraping-using-b4

@click.command()
@click.argument('word', envvar='SAYS_WORD', default='hei')
@click.option('--silent', is_flag=True, envvar='SAYS_SILENT')
def main(word, silent):

    # http://ordbok.uib.no/perl/ordbok.cgi?OPP=+hei&ant_bokmaal=5&ant_nynorsk=5&ordbok=bokmaal
    
    click.echo(word)

    url = 'http://ordbok.uib.no/perl/ordbok.cgi'
    params = dict(OPP=word)
    r = requests.get(url, params=params)

    soup = BeautifulSoup(r.text, 'html.parser')

    for span in soup.find_all('span', class_='doeme kompakt'):
        span.decompose()
        #span.unwrap()

    for span in soup.find_all('div', class_='doeme utvidet'):
        span.decompose()
        #span.unwrap()

    for div in soup.find_all('div', class_='doemeliste kompakt'):
        div.decompose()
        #span.unwrap()

    for div in soup.find_all('div', class_='tyding kompakt'):
        div.decompose()
        #span.unwrap()

    for div in soup.find_all('span', class_='kompakt'):
        div.decompose()
        #span.unwrap()

    article = soup.find('div', class_='artikkelinnhold')
    utvidet_elements = article.find_all('div', class_='utvidet')

    for utvidet_element in utvidet_elements:
        print()
        print(re.sub(' +', ' ', utvidet_element.get_text(' ')))

    if not silent:
        pass

if __name__ == "__main__":
    main()
