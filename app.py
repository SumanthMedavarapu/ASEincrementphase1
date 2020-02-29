
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
 
@app.route("/")
def home():
    return render_template("index.html")

print("hai")
 
@app.route("/get")
def getBotResponse():
    userText = request.args.get('msg')
    print("hai")
    return str(english_bot.get_response(userText))


 
if __name__ == "__main__":
    app.run()
