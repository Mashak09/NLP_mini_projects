from transformers import pipeline
qa_pipeline=pipeline('question-answering')
context='Don movie was released in 2006. It was directed by Farhan Akhtar and starred Sharukh khan and Priyanka Chopra.'
question='Who directed the movie Don?'
result=qa_pipeline(question=question, context=context)
print('answer:',result['answer'])