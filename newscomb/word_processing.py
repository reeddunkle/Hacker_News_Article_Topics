"""
    word_processing
    ~~~~~~~~~~~~~~~

    Process text for keyword and LDA models
"""



from nltk.collocations import BigramCollocationFinder
import numpy as np
import nltk
import os



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

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    total = len(articles)

    for i, article in enumerate(articles):

        title, text, url = article
        article_number = i + 1

        if title != '':

            try:
                clear_screen()

                colls = generate_collocations(text)

                print("Article {}/{}".format(article_number, total))
                print('---------------')
                print("{}\n".format(title))
                print("Link: {}\n".format(url))
                print("Topics:")



                output = ""
                for tup in colls:
                    word1, word2 = tup
                    output += "{} {}; ".format(word1, word2)

                print(output[:-2])
                print('---------------\n')

                print("Press ENTER for next article or any key to exit.")
                user_input = raw_input("> ")
                if user_input:
                    exit(0)

            except TypeError:
                continue

        else:
            continue

        clear_screen()


def display_LDA_topics(topic_word, vocab, number_words):
    '''
    Given list of topic words from LDA model, PRINTS topic words for topic (no return).
    '''

    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-number_words:-1]
        print('Topic {}: {}\n'.format(i, ' '.join(topic_words)))
