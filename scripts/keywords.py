"""
    keywords
    ~~~~~~~~

    Extract keywords from text in data/articles.csv
"""



from newscomb.text_cleanup import normalize_articles_for_collocation
from newscomb.word_processing import display_collocations
from newscomb.extract import extract_titles_text_and_urls



if __name__ == '__main__':

    articles_list = extract_titles_text_and_urls()
    collocation_ready_articles = normalize_articles_for_collocation(articles_list)
    display_collocations(collocation_ready_articles)