from flask import Flask, render_template, request, redirect, url_for #Tomas showed me how to make HTML pages work with Flask
import hashlib
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
  return '<b>Hello</b>'
  
if __name__ == '__main__':
    app.run(debug=True)
