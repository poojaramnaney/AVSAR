from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bluecosmic')
def home():
    return render_template('index.html')

    #return "<h1>Wgmig </h1>"""


if __name__ == "__main__":
    app.run(debug=True)

"""from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

if __name__ == "__main__":
    app.run(debug=True)"""
"""
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args['name']
    return HELLO_HTML.format(
        name, str(datetime.now()))


HELLO_HTML = """
"""
    <html><body>
        <h1>Hello, {0}!</h1>
        The time is {1}.
    </body></html>
"""
"""

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)"""