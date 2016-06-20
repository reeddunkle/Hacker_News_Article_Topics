<img src="http://i.imgur.com/TxS4faf.png">

## LOG

A place to document some of the interesting stages of this project


June 2, 2016
----

I was asked to present on this at [RC](https://www.recurse.com/). My collaborator and I wanted something more interesting to show than our fragile scraper, so we filtered out the stop words, compiled all of the remaining article text into one giant string, and rendered the word cloud above.

Dan leaves for his new job, and I don't touch it for a while.


June 14, 2016
----

[Rachel](https://github.com/macroscopicentric), a fellow RCer, offers to help me get going.

I am set on trying to use the [LDA](https://pythonhosted.org/lda/index.html) library that Dan had showed me. It promises to accomplish a lot, and seems to only require that I clean the text. The text needs to be coerced into a structure called a document-term matrix, but I'll get to that later...

Rachel looks around the NLTK for ideas, and suggests their collocation models.


June 15, 2016
----

I find this [custom LDA model implementation](https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html) using [Gensim](http://rare-technologies.com/?s=gensim). I'd been wanting to play with Gensim for a while, so this was an awesome introduction to a tip of its iceburg.

This also lets me avoid the LDA library's data structure, and build my own.

I work through the Gensim-derived model several times, playing around with different options. None of them seem to be *that* great.

I decide to try NLTK collocations to compare.


June 16, 2016
----

I get Rachel to show me what she found with the collocation models. We make a script to clean the text, and I set in to implementing NLTK's toy-box collocation model.

It's better than the LDA models I came up with, but the toy-box model is weak. You can see in this photo that it's grabbing a lot of generic, vague words that aren't interesting:

<img src="http://i.imgur.com/Jcz2xQw.png" />


June 17, 2016
----

I dive into the NLTK, and start crafting a custom collocation model.


June 18, 2016
----

I finish the custom model, but discover various bugs in the way I was storing the articles with their titles. I also end up adding new text cleaning methods. By the end of the day, the collocation-derived topic model looks pretty darn good. It isn't perfect. But I'm pretty happy with it.

Now back to the LDA model...
