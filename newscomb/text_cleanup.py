"""
    text_cleanup
    ~~~~~~~~~~~~

    Clean text for processing.
"""

import nltk
import stop_words

def tokenize_individual_text(raw_text):
    '''
    Given raw_text, a string, return a list of tokens.
    '''

    return sum(map(nltk.word_tokenize, nltk.sent_tokenize(raw_text)), [])


def normalize_individual_text(tokens):
    '''
    Given tokens, a list of strings of all words in a text, returns a normalized list of tokens.
    '''

    filtered_list = filter(lambda w: w.isalpha(), tokens)
    lowercased_list_of_tokens = map(lambda w: w.lower(), filtered_list)

    return lowercased_list_of_tokens


def normalize_individual_text_by_title(tokens, title):
    '''
    Given text tokens and title, return tokens minus title words
    '''

    title_tokens = tokenize_individual_text(title)
    normalized_titles = normalize_individual_text(title_tokens)

    return [t for t in tokens if t not in normalized_titles]


def remove_stopwords_from_individual_text(tokens):
    '''
    Given a list of tokens, returns a list of strings without any stopwords.
    '''

    en_stop_words = stop_words.get_stop_words('en')

    return filter(lambda w: w not in en_stop_words, tokens)


def lemmatize_individual_text(tokens):
    '''
    Given a list of tokens, return a list of lemmatized strings.
    '''

    lemmatizer = nltk.WordNetLemmatizer()

    return map(lemmatizer.lemmatize, tokens)


def normalize_all_texts_for_collocation(articles):
    '''
    Given a tuple of title list and text list, tokenize and normalize each text.
    '''

    title_list, text_list = articles

    normalized_texts = []
    for i, text in enumerate(text_list):
        raw_tokens = tokenize_individual_text(text)
        tokens_minus_title = normalize_individual_text_by_title(raw_tokens, title_list[i])
        normalized_tokens = normalize_individual_text(tokens_minus_title)

        normalized_texts.append(normalized_tokens)

    return normalized_texts


def normalize_all_texts_for_lda(texts):
    '''
    Given a list of texts: tokenize, normalize, remove stopwords, and lemmatize each text.
    '''

    normalized_texts = normalize_all_texts_for_collocation(texts)
    texts_without_stopwords = [remove_stopwords_from_individual_text(text) for text in normalized_texts]
    lemmatized_texts = [lemmatize_individual_text(text) for text in texts_without_stopwords]

    return lemmatized_texts


def normalize_titles(title_list):
    '''
    Given list of titles, returns list of text-normalized titles.
    '''

    clean_titles = []

    for t in title_list:
        title_tokens = tokenize_individual_text(t)
        normalized_title_tokens = filter(lambda w: w.isalpha(), title_tokens)
        title_string = ' '.join(normalized_title_tokens)
        clean_titles.append(title_string)

    return clean_titles
