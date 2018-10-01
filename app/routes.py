from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('../ZachSiteDB.db')
conn.execute('''CREATE TABLE if not exists projects (projid INTEGER PRIMARY KEY, projname TEXT NOT NULL, desc TEXT NOT NULL, link TEXT NOT NULL, img TEXT);''')

projname = "COOL PROJECT"
desc = "The coolest project ever."
link = "https://www.google.com"
img = ""

t = (projname, desc, link, img)
conn.execute('INSERT INTO projects (projname, desc, link, img) VALUES (?,?,?,?)', t)
conn.commit()
conn.close()

@app.route('/')
def home():
  return render_template('homeText.html')

@app.route('/projects')
def list():
   con = sqlite3.connect("../ZachSiteDB.db")
   con.row_factory = sqlite3.Row

   cur = con.cursor()
   cur.execute("SELECT * FROM projects")

   rows = cur.fetchall();
   return render_template("projects.html",rows = rows)

@app.route('/background_process_test', methods=['POST'])
def test():
    testString = request.form['searchText']
    print(testString)
    if (testString == 'projects'):
        return list()
    elif (testString == 'home'):
        return home()
    else:
        return 'nothing'

if __name__ == '__main__':
  app.run(debug=True)
