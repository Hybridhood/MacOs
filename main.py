from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)
# this is beautiful - amir
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    apple = yf.Ticker("AAPL")           # Apple’s stock symbol                 # Company major details
    hist = apple.history(period="1y")
    dates = hist.index.strftime('%m/%d/%Y').tolist()
 # Slice the list to get elements from index 1 to 3 (exclusive)
    hist = hist['Close'].tolist()  # Closing prices for the last year
      # Dates for the last year
    print(dates)
    print(hist)
    
    return render_template("about.html", dates=dates, hist=hist)
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
