import nltk
from stop_words import get_stop_words

def tokenize_individual_text(raw_text):
    '''
    Given raw_text, a string, return a list of tokens.
    '''

    return sum(map(nltk.word_tokenize, nltk.sent_tokenize(raw_text)), [])


def normalize_individual_text(tokens):
    '''
    Given tokens, a list of strings of all words in a text, returns a normalized list of strings.
    '''

    filtered_list = filter(lambda w: w.isalpha(), tokens)
    lowercased_list = map(lambda w: w.lower(), filtered_list)

    return lowercased_list


def remove_stopwords_from_individual_text(tokens):
    '''
    Given a list of tokens, returns a list of strings without any stopwords.
    '''

    import stop_words
    en_stop_words = stop_words.get_stop_words('en')

    return filter(lambda w: w not in en_stop_words, tokens)


def lemmatize_individual_text(tokens):
    '''
    Given a list of tokens, return a list of lemmatized strings.
    '''

    lemmatizer = nltk.WordNetLemmatizer()

    return map(lemmatizer.lemmatize, tokens)


def normalize_all_texts_for_collocation(corpora):
    '''
    Given a list of texts, tokenize and normalize each text.
    '''

    # skip stopwords and lemmatizing
    tokenized_texts = [tokenize_individual_text(text) for text in corpora]
    normalized_texts = [normalize_individual_text(text) for text in tokenized_texts]

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
