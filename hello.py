from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():

    #db setting
    db = pymysql.connect(
        unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
        host='localhost',
        user='root',
        password='root',
        db='testdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    #members: membersテーブル - nameカラム,emailカラム
    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members) 

@app.route('/good')
def good():
    name = "Good"
    return name

##おまじない
if __name__ == "__main__":
    app.run(debug=True)

