from flask import Flask, render_template

app = Flask(__name__)
# this is beautiful - amir
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)