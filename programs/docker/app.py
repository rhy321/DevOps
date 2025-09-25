from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
  return "hi world"

@app.route('/welcome')

def welcome():
  return "mehejhfe"

if __name__ == '__main__':
  app.run(debug = True)