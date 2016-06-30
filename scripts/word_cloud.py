"""
    word_cloud
    ~~~~~~~~~~

    Generates a word cloud from data/article.csv
"""



from wordcloud import WordCloud
from newscomb.text_cleanup import normalize_articles_for_collocation
from newscomb.word_processing import display_collocations
from newscomb.extract import generate_tuples_from_csv, extract_text_from_articles



if __name__ == '__main__':

    articles_list_html = generate_tuples_from_csv("data/articles.csv", ["title", "html", "url"])
    articles_list_text = extract_text_from_articles(articles_list_html)
    collocation_ready_articles = normalize_articles_for_collocation(articles_list_text)
    titles_tuples, text_tuples, urls_tuples = zip(*collocation_ready_articles)

    titles_list = list(titles_tuples)
    text_list = list(text_tuples)


    text = ' '.join(sum(text_list, []))

    cloud = WordCloud().generate(text)

    image = cloud.to_image()
    image.show()
