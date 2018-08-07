from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    players = ["matt la blanc", "bob bob", "moses", "leonardo de caprio"]
    return render_template("index.html")


if __name__ == '__main__':
   app.run(debug = True)