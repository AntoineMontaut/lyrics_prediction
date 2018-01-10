import os
import numpy as np

artists = ['megadeth', 'beatles', 'direstraits', 'eminem', 'madonna']
lyrics = {}

for artist in artists:
	path = 'lyrics/' + artist + '/'
	lyrics[artist] = []
	for filename in os.listdir(path):
		with open(path+filename, 'r', encoding='utf-8') as f:
			text = f.read().replace('\n', ' ')
			lyrics[artist].append(text)

X = []
y = []
for artist in artists:
	X += lyrics[artist]
	y += [artist]*len(lyrics[artist])

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import model_selection

Xtrain, Xtest, ytrain, ytest = model_selection.train_test_split(X, y, test_size = 0.2)

alpha = 0.5

model = Pipeline([
	('vectorizer', CountVectorizer(min_df=3, ngram_range=(1,1))),
	('tfidf_transformer', TfidfTransformer()),
	('bayes_model', MultinomialNB(alpha=alpha)),
])

model.fit(Xtrain, ytrain)

vect = model.named_steps['vectorizer']
# print(len(vect.vocabulary_))

print('alpha = {}'.format(alpha))
print('Accuraccy for training set: {}'.format(round(model.score(Xtrain, ytrain), 3)))
print('Accuraccy for test set: {}'.format(round(model.score(Xtest, ytest), 3)))
print('\n')

# print(model_selection.cross_val_score(model, X, y, cv=10, scoring='accuracy'))

text_list = ["take the 8mile road in detroit", "alone in the dark", 'Mind control penetrating deeper',
	'When its dog eat dog, you are what you eat', 'This never-ending nightmare']
for text in text_list:
	print('Predicted artist for "{}" is:'.format(text))
	print(model.predict([text])[0])
	print('\n')

names = np.array(model.named_steps['vectorizer'].get_feature_names())

coef = model.named_steps['bayes_model'].coef_
coef = coef.reshape((len(names),))

# Top 20 words for 1st artist
indices = (-coef).argsort()[:20].tolist()
print(names[indices])

# Top 20 words for 2nd artist
indices = (coef).argsort()[:20].tolist()
print(names[indices])