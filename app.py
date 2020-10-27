from flask import Flask, render_template
from flask import request, render_template_string
import os


# FLASK_APP = app.py

app = Flask(__name__, static_folder="static")
app.secret_key = "flag goes here"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        update = request.form['quote']
    else:
        update = "Someone once said this I think"
    
    template = '''
    %s''' % update
    quote = render_template_string(template)
    return render_template("index.html", quote = quote)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")