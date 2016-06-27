"""
    LDA_topic_models
    ~~~~~~~~~~~~~~~~

    Generate topic models using LDA for texts from data/articles.csv
"""


import argparse
from newscomb.text_cleanup import normalize_all_texts_for_lda
from newscomb.word_processing import display_LDA_topics
from newscomb.extract import extract_titles_text_and_urls
from sklearn.feature_extraction.text import CountVectorizer
import lda



def gen_parser():
    '''
    Creates command-line parser to access --topics and --words flags.
    '''

    parser = argparse.ArgumentParser(description='Manipulate an image.')
    parser.add_argument('-t', '--topics', dest='topics', required=True, nargs='?', default=0, type=int, help='Set the number of topics to generate.')
    parser.add_argument('-w', '--words', dest='words', required=True, nargs='?', default=0, type=int, help='Set the number of topic words')

    return parser


def get_texts_for_lda():
    '''
    Fetches article text from data/articles, returns lda-ready tokens
    '''

    articles_list = extract_titles_text_and_urls()
    titles_list, text_list, urls_list = zip(*articles_list)

    return normalize_all_texts_for_lda(text_list)


def create_matrix_and_vocab(texts):
    '''
    Given text tokens, returns document-term matrix
    '''

    # max_df excludes any word that appears more than (x * 100)% of the time
    # min_df requires a word to appear at least y times
    cv = CountVectorizer(max_df=.4, min_df=3)
    mat = cv.fit_transform([' '.join(x) for x in texts])
    vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]

    return (mat, vocab)


def generate_LDA_topics(matrix, number_topics):
    '''
    Given matrix and number of topics, generates LDA topic model and returns list
    '''

    model = lda.LDA(n_topics=number_topics, n_iter=400)
    model.fit(matrix)

    topic_word = model.topic_word_

    return model.topic_word_


if __name__ == '__main__':

    parser = gen_parser()
    args = parser.parse_args()
    number_topics = args.topics
    number_words = args.words

    texts_for_LDA = get_texts_for_lda()
    mat, vocab = create_matrix_and_vocab(texts_for_LDA)
    topic_words = generate_LDA_topics(mat, number_topics)

    display_LDA_topics(topic_words, vocab, number_words)
