"""
    topic_modeling
    ~~~~~~~~~~~~~~

    Generate topic models from article text
"""

from stop_words import get_stop_words
from gensim import corpora, models
from goose import Goose
from nltk.collocations import BigramCollocationFinder
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import numpy as np
import gensim
import lda
import pandas

# Goose is a library to extract data and media from sites
goose = Goose()

from text_cleanup import (tokenize_individual_text,
                          normalize_individual_text,
                          remove_stopwords_from_individual_text,
                          normalize_all_texts_for_collocation,
                          normalize_individual_text_by_title,
                          normalize_titles)




def safely_get_content(html):
    '''
    Given html: Uses goose to extract title and clean text.
    '''

    try:
        article = goose.extract(raw_html=html)
        title = article.title
        text = article.cleaned_text
        content = (title, text)

    except (IndexError, TypeError, RuntimeError):
        return None

    return content


def extract_title_and_text_from_html(html_list):
    '''
    Given a list of each article's html, returns list of tuples
    containing extracted titles and text.
    '''

    import multiprocessing
    pool = multiprocessing.Pool(12)

    articles_list = pool.map(safely_get_content, html_list)
    articles_list = [a for a in articles_list if a is not None]

    return articles_list


def transpose_tuples_lists(tuple_list):
    '''
    Given a list of tuples, return a single tuple of lists.
    '''

    title_list = []
    article_list = []

    for title, article in tuple_list:
        title_list.append(title)
        article_list.append(article)

    return (title_list, article_list)


def generate_collocations(tokens):
    '''
    Given list of tokens, return collocations
    '''

    ignored_words = nltk.corpus.stopwords.words('english')
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    # Best results with window_size, freq_filter of: (2,1) (2,2) (5,1)
    finder = BigramCollocationFinder.from_words(tokens, window_size = 2)
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    finder.apply_freq_filter(1)

    colls = finder.nbest(bigram_measures.likelihood_ratio, 5)

    return colls


def display_collocations(articles):
    '''
    Given tuple containing title list and token list, PRINTS results (no return)
    '''

    title_list, token_list = articles

    for i, tokens in enumerate(token_list):
        if title_list[i] != '':
            print('-'*15)
            title = title_list[i]
            print("Title: {}\n".format(title))
            print("Topics:")
            colls = generate_collocations(tokens)

            output = ""

            for tup in colls:
                word1, word2 = tup
                output += "{} {}; ".format(word1, word2)


            print(output[:-2])
            print('-'*15)

        else:
            pass


""" This is for LDA"""
def create_document_term_matrix(texts):
    '''
    Given list of texts, returns a document-term matrix
    '''

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    return corpus


def display_LDA_topics(topic_word):
    '''
    Given list of topic words from LDA model, PRINTS topic words for topic (no return)
    '''

    n_top_words = 34
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))


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