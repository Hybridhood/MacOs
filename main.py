from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)
# this is beautiful - amir
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    apple = yf.Ticker("AAPL")           # Apple’s stock symbol
    info = apple.info                   # Company major details
    hist = apple.history(period="1y")
    dates = hist["Close"].tolist()  # Closing prices for the last year

    
    return render_template("about.html", dates=dates, hist=hist)
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
