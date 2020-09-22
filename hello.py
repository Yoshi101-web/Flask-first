from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return render_template('hello.html', title='flask test', name=name)

@app.route('/good')
def good():
    name = "Good"
    return name

##おまじない
if __name__ == "__main__":
    app.run(debug=True)

