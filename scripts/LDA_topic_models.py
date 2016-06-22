"""
    LDA_topic_models
    ~~~~~~~~~~~~~~~~

    Generate topic models using LDA for texts from data/articles.csv
"""


from newscomb.text_cleanup import (extract_title_and_text_from_html,
                                  normalize_titles,
                                  normalize_all_texts_for_lda)
from newscomb.word_processing import (transpose_tuples_lists,
                                     display_collocations,
                                     display_LDA_topics)
from newscomb.extract import extract_titles_and_text
import lda
from sklearn.feature_extraction.text import CountVectorizer




if __name__ == '__main__':

    title_list, text_list = extract_titles_and_text()
    texts_for_LDA = normalize_all_texts_for_lda(text_list)

    # max_df excludes any word that appears more than x * 100 % of the time
    # min_df requires a word to appear at least y times
    cv = CountVectorizer(max_df=.4, min_df=3)

    mat = cv.fit_transform([' '.join(x) for x in texts_for_LDA])
    mat.shape
    model = lda.LDA(n_topics=8, n_iter=400)
    model.fit(mat)

    vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
    topic_word = model.topic_word_

    display_LDA_topics(topic_word, vocab)