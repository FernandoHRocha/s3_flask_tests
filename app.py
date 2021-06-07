from flask import Flask, render_template
from user import aws_access, aws_key
import boto3

bucket ='fhr-audio-bucket'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if app.name == '__main__':
    app.debug(True)
    app.run()

s3 = boto3.resource('s3')
