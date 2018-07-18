from flask import Flask, request, render_template, render_template_string
from vectorizer import *
from bs4 import BeautifulSoup

app = Flask(__name__)
PLACEHOLDER = "end_sentinel"
TEMPLATE_FILE = 'start.html'
soup = BeautifulSoup(open('templates/'+	TEMPLATE_FILE, 'r'))

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/', methods=['POST'])
def get_answer():
	query = request.form['query']
	q, a = return_top_result(query)
	placeholder = soup.find("div", {"id": PLACEHOLDER})
	p_question = soup.new_tag('p')
	p_question.append(q)
	p_answer = soup.new_tag('p')
	p_answer.append(' '.join(a))
	placeholder.insert_before(p_question)
	placeholder.insert_before(p_answer)
	return render_template_string(str(soup))


if __name__ == '__main__':
    app.run(debug=True, port=5000)


def return_top_result(query):
	query_vector = vectorize(query)
	q_vectors, a_vectors = get_vectors()
	question_results = multiply(query_vector, q_vectors)
	answer_results = multiply(query_vector, a_vectors)

	question_scores_to_position_dict = score_to_position_dict(question_results)
	answer_scores_to_position_dict = score_to_position_dict(answer_results)

	top_question_index = top_x_hits_from_dict(1, question_scores_to_position_dict)[0]
	question = get_questions()[top_question_index]
	answer = get_answers()[top_question_index]
	return question, answer
