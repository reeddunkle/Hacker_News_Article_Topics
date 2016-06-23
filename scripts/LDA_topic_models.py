"""
    LDA_topic_models
    ~~~~~~~~~~~~~~~~

    Generate topic models using LDA for texts from data/articles.csv
"""



from newscomb.text_cleanup import normalize_all_texts_for_lda
from newscomb.word_processing import display_LDA_topics
from newscomb.extract import extract_titles_text_and_urls
from sklearn.feature_extraction.text import CountVectorizer
import lda



if __name__ == '__main__':

    articles_list = extract_titles_text_and_urls()

    titles_list, text_list, urls_list = zip(*articles_list)

    texts_for_LDA = normalize_all_texts_for_lda(text_list)

    # max_df excludes any word that appears more than (x * 100)% of the time
    # min_df requires a word to appear at least y times
    cv = CountVectorizer(max_df=.4, min_df=3)

    mat = cv.fit_transform([' '.join(x) for x in texts_for_LDA])
    mat.shape
    model = lda.LDA(n_topics=8, n_iter=400)
    model.fit(mat)

    vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
    topic_word = model.topic_word_

    display_LDA_topics(topic_word, vocab)