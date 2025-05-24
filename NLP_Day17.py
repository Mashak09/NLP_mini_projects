def mini_chatbot(user_input):
#defines a simple chatbot function and then takes user input as a string.
    user_input=user_input.lower()#converts the suer input to lowercase
    if 'hello' in user_input:
        return 'Hello! How can i help you buddy?'
    elif 'weather' in user_input:
        return 'The current weather is sunny in weimar.'
    elif 'bye' in user_input:
        return 'Goodbye! Have a great day!'
    else:
        return'I am not sure how to respond to that my friend'
    
# Example usage
print(mini_chatbot('hows the weather today?'))
#we call the mini_chatbot function with a user input string and print the response.
    
