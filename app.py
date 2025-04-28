from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Azure App Service!</h1><p>This is a live Flask web app.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
