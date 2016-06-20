# IPython log file

from newscomb import topic_modeling
from newscomb.topic_modeling import *
import pandas
get_ipython().magic(u'paste')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd data/')
get_ipython().magic(u'paste')
title_list[2]
text_list[2]
get_ipython().system(u'pip install scikit-learn')
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv.fit(text_list)
mat = cv.fit_transform(text_list)
mat
mat[0].todense()
cv.vocabulary
cv.vocabulary_
get_ipython().magic(u'pinfo CountVectorizer')
mat.shape
import lda
model = lda.LDA(n_topics=4, n_iter=1000)
model.fit(mat)
model.topic_word_
model.doc_topic_
model.topic_word_[0].shape
model.doc_topic_[0].shape
model.doc_topic+.shape
model.doc_topic_.shape
get_ipython().magic(u'paste')
import numpy as np
get_ipython().magic(u'paste')
vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
vocab
v
In[34]
In[33]
cv.vocabulary_
vocab[495]
mat.shape
get_ipython().magic(u'paste')
n_top_words = 20
cv = CountVectorizer(max_df=.8, min_df=3)
mat = cv.fit_transform(text_list)
model = lda.LDA(n_topics=4, n_iter=1000)
mat.shape
cv = CountVectorizer(max_df=.8, min_df=2)
mat = cv.fit_transform(text_list)
mat.shape
In[33]
vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
model.fit(mat)
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().magic(u'paste')
get_ipython().system(u'pip install bs4')
from bs4 import BeautifulSoup
soup = BeautifulSoup(dataframe['html'].head(1))
soup = BeautifulSoup(dataframe['html'].head(1)[0])
soup
soup.get_text()
soup.t
soup.text
get_ipython().magic(u'paste')
get_content
import multiprocessing
pool = multiprocessing.Pool(12)
cleaned = pool.map(safely_get_content, dataframe['html'])
cleaned[0]
articles_list = cleaned
get_ipython().magic(u'logstart')
get_ipython().system(u'head ipython_log.py')
get_ipython().system(u'ls')
get_ipython().magic(u'paste')
tuple_of_lists = transpose_tuples_lists(articles_list)
title_list, text_list = tuple_of_lists

clean_title_list = normalize_titles(title_list)

collocation_ready_text = normalize_all_texts_for_collocation((clean_title_list, text_list))
articles_list = [x for x in articles_list if x is not None]
get_ipython().magic(u'paste')
tuple_of_lists = transpose_tuples_lists(articles_list)
title_list, text_list = tuple_of_lists

clean_title_list = normalize_titles(title_list)

collocation_ready_text = normalize_all_texts_for_collocation((clean_title_list, text_list))
collocation_ready_text[0]
collocation_ready_text[1]
cv = CountVectorizer(max_df=.8, min_df=2)
cv.fit(collocation_ready_text)
cv.fit([' '.join(x) for x in collocation_ready_text])
vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
model = lda.LDA(n_topics=8, n_iter=1000)
model = lda.LDA(n_topics=8, n_iter=400)
mat = cv.fit_transform([' '.join(x) for x in collocation_ready_text])
mat.shape
cv = CountVectorizer(max_df=.8, min_df=2)
mat = cv.fit_transform([' '.join(x) for x in collocation_ready_text])
mat.shape
cv = CountVectorizer(max_df=.8, min_df=3)
mat = cv.fit_transform([' '.join(x) for x in collocation_ready_text])
mat.shape
cv = CountVectorizer(max_df=.6, min_df=3)
mat = cv.fit_transform([' '.join(x) for x in collocation_ready_text])
mat.shape
cv = CountVectorizer(max_df=.4, min_df=3)
mat = cv.fit_transform([' '.join(x) for x in collocation_ready_text])
mat.shape
model = lda.LDA(n_topics=8, n_iter=400)
model.fit(mat)
vocab = [x[0] for x in sorted(cv.vocabulary_.iteritems(), key=lambda t: t[1])]
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 14
for i, topic_dist in enumerate(topic_word):
    ...     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    ...     print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    
get_ipython().magic(u'paste')
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 14
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
topic_word = model.components_  # model.components_ also works
n_top_words = 34
for i, topic_dist in enumerate(topic_word):
    ...     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    ...     print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    
get_ipython().magic(u'paste')
topic_word = model.components_  # model.components_ also works
n_top_words = 34
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
model.components_.shape
get_ipython().magic(u'pinfo model.topic_word_')
model.topic_word_.shape
model.doc_topic_
model.doc_topic_.s\hape
model.doc_topic_.shape
get_ipython().system(u'pip install seaborn')
import seaborn
import matplotlib
matplotlib.get_backend()
matplotlib.use('TkAgg'
)
seaborn.heatmap(model.doc_topic_)
from matplotlib.pylab import plt
plt.show()
fig = seaborn.heatmap(model.doc_topic_)
plt.savefig('heatmap.png')
doc_mat = model.doc_topic_
doc_mat.shape
col_means = np.mean(doc_mat, axis=1)
col_means.shape
col_means = np.mean(doc_mat, axis=2)
col_means = np.mean(doc_mat, axis=0)
col_means.shape
col_means
col_std = np.std(doc_mat, axis=0)
col_std
doc_row = doc_mat[0]
doc_row
scaled_row = (doc_row - col_means) / col_std
rescale = lambda r: (r - col_means) / col_std
scaled_row
get_ipython().magic(u'pinfo np.apply_along_axis')
rescaled_doc_mat = np.apply_along_axis(func1d=reshape, arr=doc_mat,  axis=0)
rescaled_doc_mat = np.apply_along_axis(func1d=rescale, arr=doc_mat,  axis=0)
rescaled_doc_mat = np.apply_along_axis(func1d=rescale, arr=doc_mat,  axis=1)
rescaled_doc_mat.shape
fig = seaborn.heatmap(rescaled_doc_mat)
plt.savefig('scaled_heatmap.png')
get_ipython().system(u'tail ipython_log.py')
exit()
