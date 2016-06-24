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

To scrape, run this with an optional `--count` argument to set the number of articles to scrape:

```
python scripts/hn_scrape.py --count 20
```

After you've done this, you can extract and display keywords from the articles (see first gif):

```
python scripts/keywords.py
```

You can also generate an LDA topic model:

```
python scripts/LDA_topic_models.py
```

And word clouds!

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
