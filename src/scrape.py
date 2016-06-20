"""
    scrape
    ~~~~~~~~~~~~

    Clean and normalize text for processing
"""

import requests
import pandas as pd
from exceptions import TypeError, RuntimeError



ROOT_URL = 'https://hacker-news.firebaseio.com/v0/'


def scrape_HN_articles_write_to_csv():
    '''
    Scrapes top stories on Hacker News, creates dataframe with content,
    and writes it to a .csv file.
    '''

    top_stories = requests.get(ROOT_URL + 'topstories.json').json()
    articles = []

    for article_id in top_stories:
        article = requests.get(ROOT_URL + "item/" + str(article_id) + ".json").json()
        print article  # For debugging

        if 'url' in article:
            article_url = article['url']
            try:
                article_page = requests.get(article_url)
                content = article_page.content.decode('utf-8', 'ignore')

                article_row = [article['by'], article['descendants'], article['id'], article['score'],
                     article['time'], article['title'], article['type'], article_url, content]

                articles.append(article_row)

            # Handles a ContentDecoding exception that shows up on some articles that
            # seems to occur due to lack of authentication on an article's site
            except requests.exceptions.ContentDecodingError as e:
               print('wrong password')

    df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html'])
    df.to_csv("../data/articles.csv", encoding="utf-8", index=False)


if __name__ == '__main__':
    scrape_HN_articles_write_to_csv()
