import re
from load_data import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
import re
from expander import *

def get_vectorizer():
	tfidf = TfidfVectorizer()
	stemmed_questions = get_stemmed_questions()
	stemmed_answers = get_stemmed_answers()
	tfidf.fit(stemmed_questions)
	tfidf.fit(stemmed_answers)
	return tfidf


def get_vectors():
	tfidf = get_vectorizer()
	stemmed_questions = get_stemmed_questions()
	stemmed_answers = get_stemmed_answers()
	questions_vector = tfidf.transform(stemmed_questions)
	answers_vector = tfidf.transform(stemmed_answers)
	return questions_vector, answers_vector


def vectorize(query):
	tfidf = get_vectorizer()
	vector = tfidf.transform([query])
	return vector


def stem(query):
	regex = re.compile('[^a-z0-9 ]')
	query = expandContractions(query).lower()
	clean_query = regex.sub('', query)
	print(clean_query)
	ps = PorterStemmer()
	return ' '.join([ps.stem(w) for w in clean_query.split()])


def multiply(query_vector, dataset_vector):
	print(query_vector.toarray)
	print(dataset_vector.toarray)
	return query_vector.dot(dataset_vector.transpose())


def score_to_position_dict(sparse_matrix):
	assert sparse_matrix.shape[0] == 1
	score_dict = {}
	arr = sparse_matrix.toarray()[0];
	print("arr ", arr)
	print("length of arr ", len(arr))
	for i in range(len(arr)):
		if(arr[i] > 0.0):
			score_dict[arr[i]] = i
	print("score dicct ")
	for i in score_dict:
		print(score_dict)
	return score_dict


def top_x_hits_from_dict(x, ddict):
	retval = []
	limit = min(x, len(ddict))
	print("sorted ", sorted(ddict, reverse=True))
	print("limit ", limit)
	for k in sorted(ddict, reverse=True)[:limit]:
		retval.append(ddict[k])
	return retval
