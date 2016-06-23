# Hacker News Article Topics

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

<img src="http://i.imgur.com/vbMzCNR.gif" />



To scrape, run this with an optional `--count` argument for number of articles to scrape:

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

Known bugs
----

- Goose just isn't cutting it: I'm excited about the prospect of a Python3 library I found today called [newspaper](https://github.com/codelucas/newspaper)
