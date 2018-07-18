import re
from load_data import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def get_vectorizer():
	tfidf = TfidfVectorizer()
	stemmed_questions = get_stemmed_questions()
	stemmed_answers = get_stemmed_answers()
	tfidf.fit(stemmed_questions + stemmed_answers)
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
	return tfidf.transform([query])


def multiply(query_vector, dataset_vector):
	return query_vector.dot(dataset_vector.transpose())


def score_to_position_dict(sparse_matrix):
	assert sparse_matrix.shape[0] == 1
	score_dict = {}
	arr = sparse_matrix.toarray()[0];
	for i in range(len(arr)):
		if(int(i) != 0):
			score_dict[arr[i]] = i
	return score_dict


def top_x_hits_from_dict(x, ddict):
	retval = []
	for k in sorted(ddict, reverse=True):
		retval.append(ddict[k])
	return retval
