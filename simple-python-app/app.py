from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Ml ops sample test of CI/CD Pipeline.. ALIFA KHAN'

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Listen on all interfaces
