# ASEincrementphase1

What Is A Chatbot?

chatbot is a program simulates a conversation between a user and computer

Chatbots are of 2 types
1)Rule-Based Approach 
2)Self-Learning Approach

The second approach we are using in this project using machine learning(ie, using chatterbot)

ChatterBot Library In Python
------------------------------

ChatterBot is a library in python which generates responses to user input. It uses a number of machine learning algorithms to produce 
a variety of responses.It becomes easier for the users to make chatbots using the ChatterBot library with more accurate responses.
It also allows the bot to get trained in multiple languages


How does it work?

ChatterBot makes it easier to create software so that it can engage in conversations.
Every time a chatbot saves the input ,when it gets input from user so that it helps chatbot with no knowledge
to evolve from gathered responses 


Inorder to get start with this project,we need to install the below libraries in python using pip command:

pip install flask->we are using flask micro framework in this website

pip install chatterbot

pip install chatterbot-corpus->it is the corpus of data inclined in chatterbot module and used to train the bot

steps to run the project
--------------------------
1)open your project folder in cmd,run this command "py -m venv env" to create environment

2)inorder to activate ,we need to run "env\scripts\activate"

3)set yourprojectfolder name=your main python file

4)flask run->run this command to generate localhost


process flow
---------------

1)get input from user
2)process input and return value that generated the highest confidence value from 
logic adapters
3)return response for the input
