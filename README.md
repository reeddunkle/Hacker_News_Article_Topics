# Hacker News Article Topics

<img src="http://i.imgur.com/TxS4faf.png" />

<img src="http://i.imgur.com/MppVw4T.gif" />


Installation
----

Clone the repository:

```
git clone https://github.com/reeddunkle/Hacker_News_Article_Topics.git
```

Navigate into the directory:

```
cd Hacker_News_Article_Topics
```

Make a virtual environment and activate it (recommended):

```
virtualenv venv
source venv/bin/activate
```

Install dependencies:

```
pip install .
```

Running
----

### Scrape articles from Hacker News

To scrape, run this with an optional `--count` (`-c`) argument to set the number of articles to scrape:

```
python scripts/hn_scrape.py --count 20
```

### Generate Latent Dirichlet topic model


You can generate a topic models for the corpus of articles scraped.

The required flags are `--topics` (`-t`) and `--words` (`-w`)

- `-t` sets the number of topics to generate from the corpus
- `-w` sets the numbers of words to display from each topic

```
python scripts/LDA_topic_models.py -t 10 -w 30
```

### Extract keywords for articles

You can extract and display keywords from the articles (see first gif):

```
python scripts/keywords.py
```

### Word cloud!

Generate a word cloud for the corpus of text

```
python scripts/word_cloud.py
```

**Note**
I get this error from the wordcloud library:

```
ImportError: The _imagingft C module is not installed
```

It can be solved (for me) by re-installing pillow without cache:

```
pip uninstall pillow
pip install --no-cache-dir pillow
```



Known bugs
----

- Goose just isn't cutting it: I'm excited about the prospect of a Python3 library I found today called [newspaper](https://github.com/codelucas/newspaper)
