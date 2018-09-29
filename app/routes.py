from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def homeText():
  return render_template('homeText.html')

@app.route('/oof')
def oof():
  return render_template('oof.html')

if __name__ == '__main__':
  app.run(debug=True)
