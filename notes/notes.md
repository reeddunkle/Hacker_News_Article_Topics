## LOG

A place to document some of the interesting stages of this project


June 2, 2016
----

I presented on this at [RC](https://www.recurse.com/). My collaborator and I wanted something more interesting to show than our fragile scraper, so we filtered out the stop words, compiled all of the remaining article text into one giant string, and rendered the word cloud above.

Dan leaves for his new job, and I don't touch it for a while.


June 14, 2016
----

[Rachel](https://github.com/macroscopicentric), a fellow RCer, offers to help me get going.

I am set on trying to use the [LDA](https://pythonhosted.org/lda/index.html) library that Dan had showed me. It promises to accomplish a lot, and seems to only require that I clean the text. The text needs to be coerced into a structure called a document-term matrix, but I'll get to that later...

Rachel looks around the NLTK for ideas, and suggests trying its collocation models.


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


June 20, 2016
----

| No. | Title | Keywords | Original Article |
| ----|----   |----         |----               |
|1.|"Appeals court upholds FCC net neutrality order"| internet order; Chairman Tom; open internet; FCC chairman | [Link](http://www.politico.com/story/2016/06/court-upholds-obama-backed-net-neutrality-rules-224309) |
|2.|"Appeals Court Holds Up Net Neutrality Rules In Full"| President Obama; reclassify broadband; broadband internet; service providers; act considering | [Link](http://www.npr.org/sections/thetwo-way/2016/06/14/471286113/u-s-appeals-court-holds-up-net-neutrality-rules-in-full?utm_source=facebook.com&utm_medium=social&utm_campaign=npr&utm_term=nprnews&utm_content=20160614)|
|3.|"CS GPU Programming"| also discuss; arhcitecture high; beyond covering; equivalent systems; financial modeling | [Link](http://courses.cms.caltech.edu/cs179/)|
|4.|"A few months ago I brought to light the insane state of today"| -- |[Link](https://plus.google.com/+ArtemRussakovskii/posts/VgrLdYcoifr)|
|5.|"Project Successfully Completes Security Audit"| open source; sos fund; ncc group; serious issues; adoption matched |[Link](https://www.phpmyadmin.net/news/2016/6/13/phpmyadmin-project-successfully-completes-security-audit/) |
|6.|"Analyzing Listening History"| play counts; Musicbrainz API; artist details; code used; GitHub repo | [Link](http://geoffboeing.com/2016/05/analyzing-lastfm-history/)|
|7.|"Habitat Automation That Travels with the App" | application instead; behave consistently; bits download; build deploy; get involved | [Link](https://www.habitat.sh/) |
|8.|"Checked C Microsoft Research"| system software; buffer overruns; compiler implementation; incorrect type; precise control | [Link](http://research.microsoft.com/en-us/projects/checkedc/)|
|9.|"A Sticky Stringy Quandary"| horrible performance; string situation; deriving mechanism; pretty printer; show class | [Link](http://www.stephendiehl.com/posts/strings.html) |


*Note: my output isn't a nicely formatted table like this.*

Right now it tries to identify key words from an article.
You can see the original articles to compare:

These key words are arrived at using NLTK's collocations. I established custom bigram measures, playing around with all of the options I found [here](http://www.nltk.org/howto/collocations.html). That page explains the logic behind the various ways you can refine the collocation measures for precision.

I got the best results by

- Filtering out stop words
- Collecting bigrams (versus tri-, quad-, n-grams)
- Using NLTK's BigramCollocationFinder with a window_size of 2
- Leaving the frequency filter (freq) at 1
- Collecting the 5 best

These last three choices are all very debatable design desicions. I got quite good results with a window_size of 5 and freq of 1.

And looking at the results, maybe it is better to only display the 4 best results, maybe less.