from flask import Flask
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])

def welcome():
    return "Hello World! can canbolat"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')