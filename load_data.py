import pickle

def get_questions():
	return pickle.load(open('questions.txt', 'rb'))

def get_stemmed_questions():
	return pickle.load(open('stemmed_questions.bin', 'rb'))


def get_answers():
	# will be an array of arrays of answer parts
	return pickle.load(open('answers.txt', 'rb'))

def get_stemmed_answers():
	return pickle.load(open('stemmed_answers.bin', 'rb'))


