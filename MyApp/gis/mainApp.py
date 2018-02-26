from flask import Flask, render_template, request
from bokeh.embed import components
from MyApp.gis.getFigGeography import figGeography
from bokeh.models import HoverTool
app = Flask(__name__)

@app.route("/geography")
def geography():
    script , div = components(figGeography)
    return render_template("page0.html",script=script,div=div,)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)