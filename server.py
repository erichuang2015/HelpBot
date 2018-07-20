from flask import Flask, request, render_template, render_template_string
from vectorizer import *

app = Flask(__name__)
PLACEHOLDER = "end_sentinel"
TEMPLATE_FILE = 'start.html'

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/', methods=['POST'])
def get_answer():
	query = request.form['query']
	q, a = return_top_x_results(query, 5)
	
	return render_template(TEMPLATE_FILE, questions = q, answers = a, query_string=query)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



def return_top_x_results(query, x):
	clean_query = stem(query)
	print("1 "+clean_query)
	query_vector = vectorize(clean_query)
	# print("2 ",query_vector.toarray())
	q_vectors, a_vectors = get_vectors()
	question_results = multiply(query_vector, q_vectors)
	answer_results = multiply(query_vector, a_vectors)
	print("3 ",question_results.toarray())
	print("4 ",answer_results.toarray())

	question_scores_to_position_dict = score_to_position_dict(question_results)
	answer_scores_to_position_dict = score_to_position_dict(answer_results)
	top_question_indices = top_x_hits_from_dict(x, question_scores_to_position_dict)
	print("5 ",top_question_indices)
	questions = [get_questions()[i] for i in top_question_indices]
	answers = [''.join(get_answers()[i]) for i in top_question_indices]
	return questions, answers
