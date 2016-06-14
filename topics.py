from exceptions import TypeError
import string
import pandas as pd
from goose import Goose
import numpy as np
import lda
from wordcloud import WordCloud

g = Goose()

df = pd.read_csv("articles.csv", index_col=False)

def get_content(html):
    return g.extract(raw_html=html).cleaned_text


df = df.transpose()

html_list = df["html"].tolist()
title_list = df["title"].tolist()

def clean_html():
    html_clean = []

    i = 0
    for html in html_list:
        print i
        try:
            if i not in skip:
                html_clean.append(get_content(html))

        except (IndexError, TypeError):
            pass

        except RuntimeError:
            skip.append(i)
            pass

        i += 1

    return html_clean

html_clean = clean_html()



printable = set(string.printable)
exclude = set(['!', '"', '%', '$', "'", '&', ')', '(', '*', '-', ',', '/', '.', ';', ':', '<', '?', '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}', '|', '~'])
clean_text = []
for text in html_clean:
    clean = filter(lambda c: c in printable and c not in exclude, text)
    clean_text.append(clean)


def clean(text):
    new_s = filter(lambda c: c in printable, text)
    print(len(new_s))
    clean_s = ""
    for i, c in enumerate(new_s):
        print(i)
        if (c in exclude) and (i < len(new_s) - 1):
            if new_s[i+1] != " ":
                clean_s += c
        elif i == len(new_s):
            if c not in exclude:
                clean_s += c
        else:
            clean_s += c

    return clean_s


for text in html_clean:
    good_text = clean(text)
    clean_text.append(good_text)
    print(good_text)


clean_text_lists = []
for text in clean_text:
    text_list = text.split(" ")
    clean_text_lists.append(text_list)

content_titles_strings = dict(zip(title_list, clean_text))
content_titles_strings = dict(zip(title_list, clean_text_lists))


extracted_content = dict(zip(title_list, clean_clean))


model = lda.LDA(n_topics=len(extracted_content), n_iter=2000, random_state=1)
model.fit(extracted_content[])
