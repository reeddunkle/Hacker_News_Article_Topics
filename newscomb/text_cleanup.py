"""
    text_cleanup
    ~~~~~~~~~~~~

    Clean text for processing.
"""



from newscomb.word_processing import tokenize_individual_text
import nltk
import stop_words
import multiprocessing
import string
from goose import Goose

# Goose is a library to extract text from articles
# TODO: Use beautifulsoup?
goose = Goose()



def safely_get_content(articles):
    '''
    Given html: Uses goose to extract title and clean text.
    '''

    title, html, url = articles

    try:
        article = goose.extract(raw_html=html)
        text = article.cleaned_text
        content = (title, text, url)

    except (IndexError, TypeError, RuntimeError):
        return None

    return content


def extract_text_from_html(articles):
    '''
    Given a list of each article's html, returns list of tuples
    containing extracted titles and text.
    '''

    pool = multiprocessing.Pool(12)

    articles_list = pool.map(safely_get_content, articles)
    articles_list = [a for a in articles_list if a is not None]

    return articles_list


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


def normalize_text_for_collocation(title, text):
    '''
    Given text, cleans and prepares text for collocations.
    '''

    raw_tokens = tokenize_individual_text(text)
    tokens_minus_title = normalize_individual_text_by_title(raw_tokens, title)
    normalized_tokens = normalize_individual_text(tokens_minus_title)

    return normalized_tokens


def normalize_all_texts_for_lda(texts):
    '''
    Given a list of texts: tokenize, normalize, remove stopwords, and lemmatize each text.
    '''

    lda_texts = []

    for text in texts:
        raw_tokens = tokenize_individual_text(text)
        normalized_tokens = normalize_individual_text(raw_tokens)
        tokens_minus_stopwords = remove_stopwords_from_individual_text(normalized_tokens)
        lemmatized_texts = lemmatize_individual_text(tokens_minus_stopwords)

        lda_texts.append(lemmatized_texts)

    return lda_texts


def normalize_title(title):
    '''
    Given title, returns cleaned title.
    '''

    printable = set(string.printable)
    new_title = filter(lambda c: c in printable, title)

    return new_title


def normalize_articles_for_collocation(articles):
    '''
    Given list of article tuples (title, text, url), returns list
    of tuples with everything prepared for processing.
    '''

    clean_articles = []

    for article in articles:

        title, text, url = article

        clean_title = normalize_title(title)
        collocation_ready_text = normalize_text_for_collocation(clean_title, text)

        clean_articles.append((clean_title, collocation_ready_text, url))


    return clean_articles


