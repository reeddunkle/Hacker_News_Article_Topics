# hn_scrape

*In development*

#### What it does so far:

- Scrapes the top-articles on [Hacker News](https://news.ycombinator.com/)
- Gives new definition to Big Data!

<img src=http://i.imgur.com/TxS4faf.png>


#### It also:

- Exports the article information to a .csv file, including the raw HTML

#### You can do more...

- Use [goose-extractor](https://pypi.python.org/pypi/goose-extractor/) to extract the text from the HTML
- Analyze article text using NLP techniques

#### ...but there are bugs

See Line 41 for hacky code*:

<img src=http://i.imgur.com/J1dd4Ip.png>

----

We were asked to present on this at RC last Thursday, to show our progress. We wanted something interesting to show, so we filtered out the stop words, compiled all of the remaining article text into one giant string, and rendered the word cloud above.

<img src=http://i.imgur.com/Djadd1S.png>

----

#### Goals

- Create frequency distributions of article text
- Look to extract / identify themes from a given set of articles


#### Known bugs

- *Some of the articles were causing the scraper to reach max recursion depth
- **Today I learned you can't catch RuntimeErrors
- The 'Descendants' category isn't reliable:

<img src=http://i.imgur.com/fdiMhXn.png>
