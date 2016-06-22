"""
    extract_titles_and_text
    ~~~~~~~~~~~~~~~~~~~~~~~

    Extract titles and text from data/articles.csv
"""



from newscomb.text_cleanup import extract_title_and_text_from_html
from newscomb.word_processing import transpose_tuples_lists
import pandas



def extract_titles_and_text():

    dataframe = pandas.read_csv("data/articles.csv", index_col=False)

    html_list = dataframe['html']
    articles_list = extract_title_and_text_from_html(html_list)

    tuple_of_lists = transpose_tuples_lists(articles_list)
    title_list, text_list = tuple_of_lists

    return (title_list, text_list)