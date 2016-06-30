"""
    extract
    ~~~~~~~

    Extract titles and text from data/articles.csv
"""



from newscomb.text_cleanup import extract_text_from_html
import pandas as pd



def extract_titles_text_and_urls(csv_file, headers=[]):
    '''
    Reads data/articles.csv, returns list of zipped tuples
    '''

    dataframe = pd.read_csv(csv_file, index_col=False)

    df_zero = dataframe[headers[0]]
    df_one = dataframe[headers[1]]
    df_two = dataframe[headers[2]]

    list_of_tuples_with_html = list(zip(df_zero, df_one, df_two))
    list_of_tuples_text = extract_text_from_html(list_of_tuples_with_html)

    return list_of_tuples_text
