# -*- coding: utf-8 -*-

import os

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
    url = 'http://ordbok.uib.no/perl/ordbok.cgi'
    params = dict(OPP=word)
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')
    word_soup = soup.find('div', class_='bob_kolonnenb')

    #for match in word_soup.findAll('span'):
    #    match.unwrap()
    for span in word_soup.find_all('span', class_='tydingC kompakt'):
        print(span['style'])
        if span.get('style') == 'display: inline;':
            print(found.get_text())

#    for table in word_soup.findAll('table'):
#        for row in table.findAll('tr'):
#            for cell in row.findAll('td'):
#                for div in cell.find_all('div', class_='tyding_utvidet'):
#                    print(div.get_text())
    #click.echo(word_soup.find('div', class_='artikkelinnhold'))

    if not silent:
        click.echo('not silent')

if __name__ == "__main__":
    main()
