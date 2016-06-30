"""
    keywords
    ~~~~~~~~

    Extract keywords from text in data/articles.csv
"""



from newscomb.text_cleanup import normalize_articles_for_collocation
from newscomb.word_processing import display_collocations
from newscomb.extract import generate_tuples_from_csv, extract_text_from_articles



if __name__ == '__main__':

    articles_list_html = generate_tuples_from_csv("data/articles.csv", ["title", "html", "url"])
    articles_list_text = extract_text_from_articles(articles_list_html)

    collocation_ready_articles = normalize_articles_for_collocation(articles_list_text)
    display_collocations(collocation_ready_articles)
