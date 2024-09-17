from flask import Flask, render_template, request, redirect, url_for #Tomas showed me how to make HTML pages work with Flask
import hashlib
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
  return '<b>Hello</b>'\
    '<br>'\
    '<body>'\
    '<a href="/PinkFloyd/Meddle/Echoes">Echoes</a>'\
    '</body>'
  
@app.route('/PinkFloyd/Meddle/Echoes')
def PinkFloyd_Meddle_Echoes():
   return render_template('play.html')

# @app.route('/PinkFloyd/Meddle/Echoes.png')
# def PFechoesMP3():
#    return '/workspaces/Musica/PinkFloyd/Meddle/ Echoes.mp3'

if __name__ == '__main__':
    app.run(debug=True)
