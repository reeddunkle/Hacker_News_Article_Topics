import requests
import pandas as pd

ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

for id in top:
    a = requests.get(ROOT + "item/" + str(id) + ".json").json()
    print a

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

