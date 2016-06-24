"""
    word_cloud
    ~~~~~~~~~~

    Generates a word cloud from data/article.csv
"""



from wordcloud import WordCloud
from newscomb.text_cleanup import normalize_articles_for_collocation
from newscomb.word_processing import display_collocations
from newscomb.extract import extract_titles_text_and_urls



if __name__ == '__main__':

    articles_list = extract_titles_text_and_urls()
    collocation_ready_articles = normalize_articles_for_collocation(articles_list)
    titles_tuples, text_tuples, urls_tuples = zip(*collocation_ready_articles)

    titles_list = list(titles_tuples)
    text_list = list(text_tuples)


    text = ' '.join(sum(text_list, []))

    cloud = WordCloud().generate(text)

    image = cloud.to_image()
    image.show()