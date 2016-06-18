from nltk.collocations import BigramCollocationsFinder
import nltk


def generate_collocations(tokens):
    '''Given list of tokens, return collocations
    '''

    ignored_words = nltk.corpus.stopwords.words('english')
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    finder = BigramCollocationsFinder.from_words(tokens, window_size = 4)
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    finder.apply_freq_filter(2)

    return finder.nbest(bigram_measures.likelihood_ratio, 5)

