from flask import Flask,render_template,redirect,url_for,request

from werkzeug.utils import redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/results/<marks>')
def results(marks):
    return redirect(url_for('sucess',marks=marks))

@app.route('/sucess')

def sucess():
    number = request.args.get('marks')
    if (int(number) > 40):
        return "PASS"
    else:
        return 'FAIL'


if __name__ == '__main__':
    app.run(debug=True)
