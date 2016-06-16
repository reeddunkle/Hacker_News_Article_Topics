import requests
import pandas as pd
from goose import Goose
from exceptions import TypeError, RuntimeError

goose = Goose()

ROOT = 'https://hacker-news.firebaseio.com/v0/'

def scrape_HN_articles_write_to_csv():
    '''
    Scrapes top stories on Hacker News, creates dataframe with content,
    and writes it to a .csv file.
    '''

    top_stories = requests.get(ROOT + 'topstories.json').json()
    articles = []

    for id in top_stories:
        a = requests.get(ROOT + "item/" + str(id) + ".json").json()
        print a  # For debugging

        if 'url' in a:
            a_url = a['url']
            try:
                a_page = requests.get(a_url)
                content = a_page.content.decode('utf-8', 'ignore')

                a_row = [a['by'], a['descendants'], a['id'], a['score'],
                     a['time'], a['title'], a['type'], a['url'], content]

                articles.append(a_row)

            except requests.exceptions.ContentDecodingError as e: # handling the ContentDecoding exception
               print('wrong password')

    df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html'])
    df.to_csv("articles.csv", encoding="utf-8", index=False)


if __name__ == '__main__':
    scrape_articles_write_to_csv()
    # html_list = df["html"].tolist()
    # title_list = df['title'].tolist()
    # html_clean = clean_html(html_list)