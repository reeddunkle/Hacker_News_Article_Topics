# Hacker News Topic Model

What works so far
----

<img src="http://i.imgur.com/v5e7kLP.png" />
<img src="http://i.imgur.com/ACwzxZ9.png" />

So, it does OK. Here you can check out the original articles to compare:


| No. | Title | Topic Model | Original Article |
| ----|----   |----         |----               |
|1.|"Appeals court upholds FCC net neutrality order"| internet order; Chairman Tom; open internet; FCC chairman | [Link](http://www.politico.com/story/2016/06/court-upholds-obama-backed-net-neutrality-rules-224309) |
|2.|"Appeals Court Holds Up Net Neutrality Rules In Full"| President Obama; reclassify broadband; broadband internet; service providers; act considering | [Link](http://www.npr.org/sections/thetwo-way/2016/06/14/471286113/u-s-appeals-court-holds-up-net-neutrality-rules-in-full?utm_source=facebook.com&utm_medium=social&utm_campaign=npr&utm_term=nprnews&utm_content=20160614) |
|3.|"CS GPU Programming"| also discuss; arhcitecture high; beyond covering; equivalent systems; financial modeling | [Link](http://courses.cms.caltech.edu/cs179/)|
|4.|"A few months ago I brought to light the insane state of today"| -- |[Link](https://plus.google.com/+ArtemRussakovskii/posts/VgrLdYcoifr)|
|5.|"Project Successfully Completes Security Audit"| open source; sos fund; ncc group; serious issues; adoption matched |[Link](https://www.phpmyadmin.net/news/2016/6/13/phpmyadmin-project-successfully-completes-security-audit/) |
|6.|"Analyzing Listening History"| play counts; Musicbrainz API; artist details; code used; GitHub repo | [Link](http://geoffboeing.com/2016/05/analyzing-lastfm-history/)|
|7.|"Habitat Automation That Travels with the App" | application instead; behave consistently; bits download; build deploy; get involved | [Link](https://www.habitat.sh/) |
|8.|"Checked C Microsoft Research"| system software; buffer overruns; compiler implementation; incorrect type; precise control | [Link](http://research.microsoft.com/en-us/projects/checkedc/)|
|9.|"A Sticky Stringy Quandary"| horrible performance; string situation; deriving mechanism; pretty printer; show class | [Link](http://www.stephendiehl.com/posts/strings.html) |


This is a topic model arrived at using NLTK's collocations. I established a custom model, playing around with all of the options I found [here](http://www.nltk.org/howto/collocations.html). That page explains the logic behind the various ways you can refine the collocation model for precision.

I got the best results by

- Filtering out stop words
- Collecting bigrams (versus tri-, quad-, n-grams)
- Using NLTK's BigramCollocationFinder with a window_size of 2
- Leaving the frequency filter (freq) at 1
- Collecting the 5 best

These last three choices are all very debatable design desicions. I got quite good results with a window_size of 5 and freq of 1.

And looking at the results above, maybe it is better to only display the 4 best results, maybe less.

Known bugs
----

- I need to clean my titles more carefully: see No. 2, 3, 6, 7 above
- I'm not sure what happened with No. 4 above. It seems like an issue with Goose
- *Some of the articles cause Goose to reach max recursion depth: RuntimeError
- Sometimes an article's HTML isn't parsed correctly and Goose is passed an int instead of a string: TypeError
- IndexErrors were thrown, but I didn't log this error
- The 'Descendants' category isn't reliable:
