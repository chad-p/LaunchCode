class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


class BoredChatbot(Chatbot):

    def check_if_bored(self, prompt_from_human):

        length_of_message = len(prompt_from_human)

        if length_of_message < 20:
            return Chatbot.response(self, prompt_from_human)
        else:
            return "zzz... oh excuse me, I dozed off reading your essay."

# make a chatbot
sally = BoredChatbot("Sally")
# introduce the chatbot and allow the user to say something
human_message = input(sally.greeting())
# respond to the user
print(sally.check_if_bored(human_message))
