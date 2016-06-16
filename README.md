# Hacker News Scraper

*In development*

## What it does so far:

- Scrapes the top-articles on [Hacker News](https://news.ycombinator.com/)
- Processes the text from the article, cleaning it in preparation for the [lda](https://pythonhosted.org/lda/index.html) API
- Gives new definition to Big Data!

<img src=http://i.imgur.com/TxS4faf.png>

----

I was asked to present on this at [RC](https://www.recurse.com/) on June 2nd. My collaborator and I wanted something interesting to show, because at that point all we had was a fragile scraper, so we filtered out the stop words, compiled all of the remaining article text into one giant string, and rendered the word cloud above.

----

## TODO

- The LDA [API](https://pythonhosted.org/lda/api.html) requires text to be in a certain form. Right now I'm not certain what that form is, so I'm working on that

- Clean up code in topics.py -- I've been writing this in Jupyter's notebook, and copying in the code that I want, building up technical debt. I've got to pay that off and properly organize my code, and tidy up my scripts.

- I feel uneasy about the way that I'm handling the exceptions that some of these articles are throwing (see below). This seems to be mainly because of Goose.

  For now I have to accept this, but it is a major weakness in code. Ideally I would understand what is causing these errors, and rather than passing over those articles, I could handle them differently.


## Known bugs

- *Some of the articles cause Goose to reach max recursion depth: RuntimeError
- Sometimes an article's HTML isn't parsed correctly and Goose is passed an int instead of a string: TypeError
- IndexErrors were thrown, but I didn't log this error
- The 'Descendants' category isn't reliable:

<img src=http://i.imgur.com/fdiMhXn.png>
