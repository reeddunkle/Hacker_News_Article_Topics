"""
    topic_modeling
    ~~~~~~~~~~~~~~

    Generate topic models from article text
"""

from stop_words import get_stop_words



from newscomb.text_cleanup import (tokenize_individual_text,
                          normalize_individual_text,
                          remove_stopwords_from_individual_text,
                          normalize_all_texts_for_collocation,
                          normalize_individual_text_by_title,
                          normalize_all_texts_for_lda,
                          normalize_titles)













if __name__ == '__main__':

    dataframe = pandas.read_csv("data/articles.csv", index_col=False)

    html_list = dataframe['html']
    articles_list = extract_title_and_text_from_html(html_list)

    tuple_of_lists = transpose_tuples_lists(articles_list)
    title_list, text_list = tuple_of_lists

    clean_title_list = normalize_titles(title_list)

    collocation_ready_text = normalize_all_texts_for_collocation((clean_title_list, text_list))

    articles = (clean_title_list, collocation_ready_text)
    display_collocations(articles)

    """--------------------------------------------------"""

    texts_for_LDA = normalize_all_texts_for_lda(text_list)

    # cv = CountVectorizer()
    # cv.fit(texts_for_LDA)

    # max_df excludes any word that appears more than x * 100 % of the time
    # min_df requires a word to appear at least y times
    cv = CountVectorizer(max_df=.4, min_df=3)
    mat = cv.fit_transform([' '.join(x) for x in texts_for_LDA])
    mat.shape
    model = lda.LDA(n_topics=8, n_iter=400)
    model.fit(mat)

    vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
    topic_word = model.topic_word_




    """
    ----------------------------
    FOR LATER LDA IMPLEMENTATION
    """





    # vocab = sum(texts_for_LDA, [])
    # titles = title_list

    # doc_term_matrix = create_document_term_matrix(texts_for_LDA)

    # model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
    # model.fit(doc_term_matrix)

    # topic_word = model.topic_word_
    # n_top_words = 8

    # for i, topic_dist in enumerate(topic_word):
    #     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    #     print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    # articles_for_lda = dict(zip(title_list, texts_for_LDA))