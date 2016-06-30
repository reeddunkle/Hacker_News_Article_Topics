"""
    extract
    ~~~~~~~

    Extract titles and text from data/articles.csv
"""



import pandas as pd
import multiprocessing
from goose import Goose

goose = Goose()  # Goose is a library to extract text from articles



def generate_tuples_from_csv(csv_file, headers=[]):
    '''
    Reads data/articles.csv, returns list of zipped tuples
    '''

    dataframe = pd.read_csv(csv_file, index_col=False)

    df_zero = dataframe[headers[0]]
    df_one = dataframe[headers[1]]
    df_two = dataframe[headers[2]]

    list_of_tuples = list(zip(df_zero, df_one, df_two))

    return list_of_tuples


def safely_get_content_from_article_html(article):
    '''
    Given articles: Uses goose to extract title from
    html and cleans the text.
    '''

    title, html, url = article

    try:
        article_text = goose.extract(raw_html=html)
        text = article_text.cleaned_text
        content = (title, text, url)

    except (IndexError, TypeError, RuntimeError):
        return None

    return content


def extract_text_from_articles(articles):
    '''
    Given a list of each article's html, returns list of tuples
    containing extracted titles and text.
    '''

    pool = multiprocessing.Pool(12)

    articles_list = pool.map(safely_get_content_from_article_html, articles)
    articles_list = [a for a in articles_list if a is not None]

    return articles_list
