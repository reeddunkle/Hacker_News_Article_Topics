"""
    extract
    ~~~~~~~

    Extract titles and text from data/articles.csv
"""



from newscomb.text_cleanup import extract_text_from_html
import pandas



def extract_titles_text_and_urls():

    dataframe = pandas.read_csv("data/articles.csv", index_col=False)

    html_list = dataframe['html']
    title_list = dataframe['title']
    url_list = dataframe['url']

    articles = list(zip(title_list, html_list, url_list))

    articles_list = extract_text_from_html(articles)

    return articles_list
