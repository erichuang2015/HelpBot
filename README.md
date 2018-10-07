# HelpBot

(A work in progress)

A simple QA system for information-retrieval that attempts to solve user queries using a corpus of data.

**How does it work?**

1. Extract `HelpBot.zip` and cd into the directory and run the following commands:  
  a. `export FLASK_APP=server.py`  
  b. `flask run`
2. Open browser and type "localhost:5000" (default port is 5000)
3. Enter your search query into the text-box and click submit.
4. You'll see results in the following format:  
  a. The entered query in <BLUE> color  
  b. A set of matching questions in <RED> and answers in <GREEN>
5. User can see which question is closest to his search query and follow those steps.


**Algorithm:**

The algorithm is a type of unsupervised learning.
The logic for matching the user query is based on the cosine-similarity of the query with existing questions/queries in the dataset.
The process consists of two parts:

1. Precomputation  
  a. The text of the docs in `SampleDocuments.zip` was separated into pairs of questions and their answers.  
  b. The text of the questions was cleaned and stemmed and saved in a separate file "stemmed_questions.bin".

2. Realtime Matching  
  a. The input query is also stemmed.  
  b. The stemmed questions are loaded from disk and used to created a TF-IDF matrix.  
  c. The stemmed input query is converted to a TF-IDF vector using the matrix created above (the tfidf matrix' vocabulary is set during the previous step).  
  d. The product of the input query vector with each question vector (from the TF-IDF matrix) is calculated, and the results are sorted by descending product score.  
  e. Top 5 scoring questions are returned, as they seem most relevant to user-query according to TF-IDF measure.


**Improvements:**

1. Currently on questions are being considered. We can also gather context from answers to get better results.
2. We are currently relying on exact words. This will fail in case the use-query has synonyms of words in the knowledge-database. We can correct this by converting the questions and answers data to word-embeddings using word2vec algo. Using this, we could find the most relevant questions in the database with the smallest Euclidean distance to the **word2vec** vector of the user-query, and should theoretically fix this edge-case.
