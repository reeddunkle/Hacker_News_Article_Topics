"""
    keywords
    ~~~~~~~~

    Extract keywords from text in data/articles.csv
"""

from newscomb.text_cleanup import normalize_titles, normalize_all_texts_for_collocation
from newscomb.word_processing import display_collocations
from newscomb.extract import extract_titles_and_text



if __name__ == '__main__':

    title_list, text_list = extract_titles_and_text()

    clean_title_list = normalize_titles(title_list)

    collocation_ready_text = normalize_all_texts_for_collocation((clean_title_list, text_list))

    articles = (clean_title_list, collocation_ready_text)
    display_collocations(articles)