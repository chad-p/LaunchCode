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

    def response(self, prompt_from_human):

        length_of_message = len(prompt_from_human)

        if length_of_message < 20:
            self.response = Chatbot.response(self, prompt_from_human)
        else:
            self.response = "zzz... oh excuse me, I dozed off reading your essay."

        return self.response


# make a chatbot
#sally = BoredChatbot("Sally")
# introduce the chatbot and allow the user to say something
#human_message = input(sally.greeting())
# respond to the user
#print(sally.check_if_bored(human_message))
print(BoredChatbot('Sally').response('123456789101112131415161718192021'))
print(BoredChatbot('Sally').response('Once upon a time in a galaxy far, far away.'))