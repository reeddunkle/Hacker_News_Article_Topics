"""
    scrape
    ~~~~~~

    Scrape and store Hacker News articles.
"""



import argparse
import requests
import pandas as pd



ROOT_URL = 'https://hacker-news.firebaseio.com/v0/'


def scrape_HN_articles_write_to_csv(count=0):
    '''
    Scrapes top stories on Hacker News, creates dataframe with content,
    and writes it to a .csv file.
    '''
    if count > 0:
        limit = int(count)
    else:
        limit = None

    print("Limit is set to: {}".format(limit))

    top_stories = requests.get(ROOT_URL + 'topstories.json').json()


    articles = []

    for article_id in top_stories[:limit]:
        article = requests.get(ROOT_URL + "item/" + str(article_id) + ".json").json()
        article_type = article['type']

        if 'url' in article and article_type == 'story':
            article_url = article['url']
            try:
                article_page = requests.get(article_url)
                content = article_page.content.decode('utf-8', 'ignore')

                article_row = [article['by'], article['descendants'], article['id'], article['score'],
                     article['time'], article['title'], article_type, article_url, content]

                articles.append(article_row)


            # A ContentDecoding exception seems to arise when attempting to scrape
            # an site that requires some sort of authentication (throws 'wrong password')
            except requests.exceptions.ContentDecodingError as e:
               print('wrong password')

    df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html'])
    df.to_csv("data/articles.csv", encoding="utf-8", index=False)


def gen_parser():

    parser = argparse.ArgumentParser(description='Manipulate an image.')
    parser.add_argument('--count', dest='count', required=False, nargs='?', default=0, type=str, help='Set the number of top articles to scrape. If none given, will scrape all')

    return parser


if __name__ == '__main__':

    parser = gen_parser()
    args = parser.parse_args()
    count = args.count

    if count.isdigit() and count >= 0:
        scrape_HN_articles_write_to_csv(count)
