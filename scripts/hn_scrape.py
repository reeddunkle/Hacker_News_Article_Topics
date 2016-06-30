"""
    scrape
    ~~~~~~

    Scrape and store Hacker News articles.
"""



import argparse
import requests
import pandas as pd
import os
import sys



ROOT_URL = 'https://hacker-news.firebaseio.com/v0/'


def scrape_HN_articles_write_to_csv(count=0):
    '''
    Scrapes top stories on Hacker News, creates dataframe with content,
    and writes it to a .csv file.
    '''

    count = int(count)

    if count > 0:
        limit = count
    else:
        limit = None

    print("Limit: {}".format(limit))

    top_stories = requests.get(ROOT_URL + 'topstories.json').json()

    article_count = 0
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

                article_count += 1
                sys.stdout.write("Articles scraped: {}\r".format(article_count))
                sys.stdout.flush()

            # A ContentDecoding exception seems to arise when attempting to scrape
            # an site that requires some sort of authentication (throws 'wrong password')
            except requests.exceptions.ContentDecodingError as e:
               print('{}: Wrong password\nSkipping article...\n'.format(e))
               continue

            except requests.exceptions.SSLError as e:
                print('{}: Verification failed. Could be dangerous.\nSkipping article...\n'.format(e))
                continue

            except requests.exceptions.ConnectionError as e:
                print('{} Connection reset by peer. This is a server-side error.\nSkipping article...\n'.format(e))


    print("Total number scraped: {}".format(article_count))
    df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html'])

    try:
        os.makedirs("data")

    except OSError:
        pass

    df.to_csv("data/articles.csv", encoding="utf-8", index=False)


def gen_parser():
    '''
    Creates command-line parser to access --count flag.
    '''

    parser = argparse.ArgumentParser(description='Get article count.')
    parser.add_argument('-c', '--count', dest='count', required=False, nargs='?', default=0, type=str, help='Set the number of top articles to scrape. If none given, will scrape all')

    return parser



if __name__ == '__main__':

    parser = gen_parser()
    args = parser.parse_args()
    count = args.count

    scrape_HN_articles_write_to_csv(count)
