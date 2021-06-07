from flask import Flask, render_template
from user import aws_access, aws_key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if app.name == '__main__':
    app.debug(True)
    app.run()