"""
    word_processing
    ~~~~~~~~~~~~~~~

    Process text for keyword and LDA models
"""



from gensim import corpora
from nltk.collocations import BigramCollocationFinder
import numpy as np
import nltk



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


def tokenize_individual_text(raw_text):
    '''
    Given raw_text, a string, return a list of tokens.
    '''

    return sum(map(nltk.word_tokenize, nltk.sent_tokenize(raw_text)), [])


def generate_collocations(tokens):
    '''
    Given list of tokens, return collocations.
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
    Given list of article tuples (title, text, url), generates and
    PRINTS collocations (no return).
    '''

    for article in articles:

        title, text, url = article

        if title != '':
            print('-' * 15)
            print("Article: {}\n".format(title))
            print("Link: {}\n".format(url))
            print("Topics:")

            colls = generate_collocations(text)

            output = ""
            for tup in colls:
                word1, word2 = tup
                output += "{} {}; ".format(word1, word2)

            print(output[:-2])
            print('-'*15)

        else:
            pass


""" For LDA"""
def create_document_term_matrix(texts):
    '''
    Given list of texts, returns a document-term matrix.
    '''

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    return corpus


def display_LDA_topics(topic_word, vocab):
    '''
    Given list of topic words from LDA model, PRINTS topic words for topic (no return).
    '''

    n_top_words = 34

    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))
