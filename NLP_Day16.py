from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
# This pipeline generates text using the GPT-2 model

text = 'i am a devops architect at a big tech firm called Nvidia'
result = generator(text, max_length=50, num_return_sequences=1)
# max_length of the output text is set to 50 tokens

print('Generated Text:', result[0]['generated_text'])
# The generated text is printed
