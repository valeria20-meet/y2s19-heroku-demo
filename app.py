from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

# 127.0.0.1:5000/ -> opens 'hello.html'
@app.route('/')
def hello_html():
    return render_template("hello.html")




if __name__ == '__main__': # This is always at the end
    app.run(debug=True)