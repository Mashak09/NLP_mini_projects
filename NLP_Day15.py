from transformers import pipeline
translator=pipeline("translation_en_to_fr")
#this pipeline translates english to french
text="I am a devops architect at a big tech firm called Nvidia"
result=translator(text,max_length=40)
#max length of the text given here is 40
print('French Translation;',result[0]['translation_text'])