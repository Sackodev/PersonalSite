from flask import Flask, render_template, request, session
import sqlite3
import csv

app = Flask(__name__)

conn = sqlite3.connect('../ZachSiteDB.db')
conn.execute('''CREATE TABLE if not exists projects (projid INTEGER PRIMARY KEY, projname TEXT NOT NULL, desc TEXT NOT NULL, link TEXT NOT NULL, img TEXT, editimg TEXT);''')

with open('app/static/csv/projects.csv') as csvfile:
    curs = conn.cursor()
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for csvrow in reader:
        curs.execute(
            'SELECT * FROM projects WHERE projname = ? LIMIT 1', (csvrow[0],))
        trow = curs.fetchone()

        if trow is None:
            t = (csvrow[0], csvrow[1], csvrow[2], csvrow[3], csvrow[4])
            curs.execute(
                'INSERT INTO projects (projname, desc, link, img, editimg) VALUES (?,?,?,?,?)', t)
        elif (csvrow[0] != trow[1] or csvrow[1] != trow[2] or csvrow[2] != trow[3] or csvrow[3] != trow[4] or csvrow[4] != trow[5]):
            t = (csvrow[0], csvrow[1], csvrow[2],
                 csvrow[3], csvrow[4], trow[0])
            curs.execute(
                'UPDATE projects SET projname=?, desc=?, link=?, img=?, editimg=? WHERE projid=?', t)

conn.commit()
conn.close()


@app.route('/')
def home():
    return render_template('layoutBox.html')


@app.route('/', methods=['POST'])
def process():
    hashID = request.form['hashID']
    print(hashID)
    if (hashID == "projects"):
        return projects()
    elif (hashID == "resume"):
        return resume()
    elif (hashID == "home"):
        return defaultCont()


def projects():
    con = sqlite3.connect("../ZachSiteDB.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()
    return render_template("projects.html", rows=rows)


def resume():
    return render_template("resume.html")


@app.route('/default')
def defaultCont():
    return render_template('contentDefault.html')


if __name__ == '__main__':
    app.secret_key = 'oihg49whg7hw4gi'
    app.run(debug=True)
