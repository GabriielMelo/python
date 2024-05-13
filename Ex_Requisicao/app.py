
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])

def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return render_template('submit.html', name=name, email=email)
if __name__ == '__main__':
    app.run(debug=True) 