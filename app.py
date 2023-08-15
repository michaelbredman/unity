from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/time')
def time():
    return '<h2>time</h2>'

if __name__ == "__main__":
    app.run(port=5001)
