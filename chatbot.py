from chatterbot import ChatBot
from colorama import *


chatbot = ChatBot("Abraham")

#Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# An input statment
print (Fore.RED + "Alace:")
print (Fore.RED + "Hello, how are you today?")

print (Fore.GREEN + "Abraham:")
# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

print (Fore.RED + "Alace:")
print (Fore.RED + "Can I ask you a question?")

print (Fore.GREEN + "Abraham:")
chatbot.get_response("Can I ask you a question?")

print (Fore.RED + "Alace:")
print (Fore.RED + "Do you love me?")

print (Fore.GREEN + "Abraham:")
chatbot.get_response("Do you love me?")
#print "Ofcourse, why would you even ask?"
