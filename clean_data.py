from nltk.stem import PorterStemmer
import re
from load_data import *
from expander import *
import pickle

PS = PorterStemmer()
REGEX_NON_ALPHA = '[^a-z]'

def replace_bad_apostrophe(string):
	return string.replace('’', "'")

def replace_non_alpha(string, replacement_char):
	regex = re.compile(REGEX_NON_ALPHA)
	return regex.sub(replacement_char, string)

def stem(string):
	return ' '.join([PS.stem(w) for w in string.split()])

def clean_and_save_questions():
	questions = get_questions()
	for i in range(len(questions)):
		questions[i] = stem(replace_non_alpha(expandContractions(replace_bad_apostrophe(questions[i].lower())), ' '))
	pickle.dump(questions, open('stemmed_questions.bin', 'wb'))

def clean_and_save_answers():
	answers = get_answers()
	for i in range(len(answers)):
		for j in range(len(answers[i])):
			answers[i][j] = stem(replace_non_alpha(expandContractions(replace_bad_apostrophe(answers[i][j].lower())), ' '))
		answers[i] = ' '.join(answers[i])
	pickle.dump(answers, open('stemmed_answers.bin', 'wb'))