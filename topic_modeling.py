from stop_words import get_stop_words
from gensim import corpora, models
from goose import Goose
import numpy
import gensim
import nltk
import lda
import pandas

goose = Goose()

from text_cleanup import (tokenize_individual_text,
                          normalize_individual_text,
                          remove_stopwords_from_individual_text,
                          lemmatize_individual_text,
                          normalize_all_texts_for_collocation,
                          normalize_all_texts_for_lda)


def get_content(html):
    '''
    Given html: Use goose to extract text and clean it.
    '''

    return goose.extract(raw_html=html).cleaned_text


def clean_html(html_list):
    html_clean = []

    article_count = 0
    for html in html_list[:20]:
        # print i
        try:
            if article_count:  # For debugging
                html_clean.append(get_content(html))

        except (IndexError, TypeError):
            pass

        except RuntimeError:
            pass

        article_count += 1

    # print(article_count)
    return html_clean


def display_collocations(articles):
    '''
    Given article dictionary of {title: text},
    returns collocations list for each text.
    '''
    i = 0
    for title, tokens in articles.iteritems():
        print('-'*15)
        # print("Should be dictionary {}: {}".format(title, tokens))

        print("Title: {}\n".format(title))
        print("Topics:")
        nltk_text = nltk.Text(tokens)
        nltk_text.collocations()
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
    title_list = dataframe['title'].tolist()
    texts_clean = clean_html(html_list)

    collocation_ready_texts = normalize_all_texts_for_collocation(texts_clean)
    articles_for_collocations = dict(zip(title_list, collocation_ready_texts))

    display_collocations(articles_for_collocations)

    texts_for_LDA = normalize_all_texts_for_lda(texts_clean)

    vocab = sum(texts_for_LDA, [])
    titles = sum(title_list, [])

    doc_term_matrix = create_document_term_matrix(texts_for_LDA)

    model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
    model.fit(doc_term_matrix)

    topic_word = model.topic_word_
    n_top_words = 8

    for i, topic_dist in enumerate(topic_word):
        topic_words = numpy.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    articles_for_lda = dict(zip(title_list, texts_for_LDA))


