# Hacker News Key Words

<img src="http://i.imgur.com/8u34rvs.gif" />
<img src="http://i.imgur.com/JabwHTV.gif" />


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


*Note: my output isn't a nicely formatted table like this yet.*


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

Right now the functionality of scraping and topic modeling is separate.

To scrape, run this with an optional `--count` argument for number of articles to scrape:

```
python newscomb/hn_scrape.py --count 20
```

After you've done this, you can extract and display keywords from the articles:

```
python newscomb/topic_modeling.py
```


Known bugs
----

- I need to clean my titles more carefully: see No. 2, 3, 6, 7 above
- I'm not sure what happened with No. 4 above. It seems like an issue with Goose
- *Some of the articles cause Goose to reach max recursion depth: RuntimeError
- Sometimes an article's HTML isn't parsed correctly and Goose is passed an int instead of a string: TypeError
- IndexErrors were thrown, but I didn't log this error
