# Hacker News Key Words

<img src="http://i.imgur.com/JabwHTV.gif" />


Installation
----

Clone the repository:

```
git clone https://github.com/reeddunkle/Hacker_News_Keywords.git
```

Navigate into the directory:

```
cd Hacker_News_Keywords
```

Make a virtual environment for the project (recommended):

```
virtualenv venv
```

Activate venv:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Running
----

<img src="http://i.imgur.com/8u34rvs.gif" />

Right now the functionality of scraping and topic modeling is separate.

To scrape, run this with an optional `--count` argument for number of articles to scrape:

```
python newscomb/hn_scrape.py --count 20
```

After you've done this, you can extract and display keywords from the articles (see first gif):

```
python newscomb/topic_modeling.py
```


Known bugs
----

- I need to clean my titles differently: currently I clean out numbers and some proper nouns
- *Some of the articles cause Goose to reach max recursion depth: RuntimeError
- Sometimes an article's HTML isn't parsed correctly and Goose is passed an int instead of a string: TypeError
- IndexErrors were thrown, but I didn't log this error
