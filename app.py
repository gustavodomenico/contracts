from flask import *
     
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["nome_a"])
        print(request.form["nome_b"])
    
    return render_template("contract.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# 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