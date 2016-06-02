import requests
import pandas as pd

ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

i = 0
for id in top:
    if i < 10:

        a = requests.get(ROOT + "item/" + str(id) + ".json").json()
        print a
        i += 1

        if 'url' in a:
            a_url = a['url']
            a_page = requests.get(a_url)

            a_row = [a['by'], a['descendants'], a['id'], a['score'], 
                     a['time'], a['title'], a['type'], a['url'], a_page.content]

            articles.append(a_row)
    else:
        pass

df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html'])

df.to_csv("articles.csv", encoding="utf-8", index=False)

