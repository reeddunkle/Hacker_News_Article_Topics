TODO
----

- [ ] Create topic models using LDA library *ideally*. If this library won't behave, I'll implement a custom script.

- [ ] I feel uneasy about the way that I'm handling the exceptions that some of these articles are throwing (see below). This seems to be mainly because of Goose.

  For now I have to accept this, but it is a major weakness in code. Ideally I would understand what is causing these errors, and rather than passing over those articles, I could handle them differently.

- [X] Create topic models using NLTK's collocations.

- [X] The LDA library [API](https://pythonhosted.org/lda/api.html) requires text to be in a certain form. Right now I'm not certain what that form is, so I'm working on that. **I've made sense of most of this now. More to come on it. (6/19/16)**

- [X] Clean up code in topics.py -- I've been writing this in Jupyter's notebook, and copying in the code that I want, building up technical debt. I've got to pay that off and properly organize my code, and tidy up my scripts.  **Refactoring isn't perfect, but I've made a lot of progress in this regard. The project has the structure it was previously lacking. (6/19/16)**