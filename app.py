from flask import Flask
     
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='color:green'>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# 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