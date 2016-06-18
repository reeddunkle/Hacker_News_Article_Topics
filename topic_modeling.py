from stop_words import get_stop_words
from gensim import corpora, models
from goose import Goose
from nltk.collocations import BigramCollocationFinder
import nltk
import numpy
import gensim
import lda
import pandas

goose = Goose()

from text_cleanup import (tokenize_individual_text,
                          normalize_individual_text,
                          remove_stopwords_from_individual_text,
                          lemmatize_individual_text,
                          normalize_all_texts_for_collocation,
                          normalize_titles,
                          normalize_all_texts_for_lda)


def get_content(html):
    '''
    Given html: Uses goose to extract title and clean text.
    '''

    article = goose.extract(raw_html=html)
    title = article.title
    text = article.cleaned_text

    return (title, text)

def extract_title_text_from_html(html_list):
    '''
    Given a list of each article's html, returns list of tuples
    containing extracted titles and text.
    '''

    articles_list = []

    article_count = 0
    for html in html_list:
        # print i
        try:
            if article_count:  # For debugging
                articles_list.append(get_content(html))

        except (IndexError, TypeError, RuntimeError):
            pass

        article_count += 1

    return articles_list


def list_of_tuples_to_tuple_of_lists(tuple_list):
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
    '''Given list of tokens, return collocations
    '''

    ignored_words = nltk.corpus.stopwords.words('english')
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationFinder.from_words(tokens, window_size = 4)
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    finder.apply_freq_filter(2)

    colls = finder.nbest(bigram_measures.likelihood_ratio, 5)

    return colls


def display_collocations(articles):
    '''
    Given article dictionary of {title: text},
    returns collocations list for each text.
    '''
    title_list, token_list, = articles
    for i, tokens in enumerate(token_list):
        print('-'*15)

        if title_list[i] != '':
            title = title_list[i]
        else:
            title = "MISSING TITLE"


        colls = generate_collocations(tokens)

        print("Title: {}\n".format(title))
        print("Topics:")
        print(colls)
        print('-'*15)


def create_document_term_matrix(texts):
    '''
    Given list of texts, returns a document-term matrix
    '''

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    return corpus



if __name__ == '__main__':

    dataframe = pandas.read_csv("articles.csv", index_col=False)

    html_list = dataframe['html'].tolist()
    # title_list = dataframe['title'].tolist()
    articles_list = extract_title_text_from_html(html_list[:12])

    tuple_of_lists = list_of_tuples_to_tuple_of_lists(articles_list)
    title_list, text_list = tuple_of_lists

    clean_title_list = normalize_titles(title_list)

    collocation_ready_text = normalize_all_texts_for_collocation(text_list)

    articles = (clean_title_list, collocation_ready_text)

    display_collocations(articles)

    # texts_for_LDA = normalize_all_texts_for_lda(texts_clean)

    # vocab = sum(texts_for_LDA, [])
    # titles = title_list

    # doc_term_matrix = create_document_term_matrix(texts_for_LDA)

    # model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
    # model.fit(doc_term_matrix)

    # topic_word = model.topic_word_
    # n_top_words = 8

    # for i, topic_dist in enumerate(topic_word):
    #     topic_words = numpy.array(vocab)[numpy.argsort(topic_dist)][:-(n_top_words+1):-1]
    #     print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    # articles_for_lda = dict(zip(title_list, texts_for_LDA))


