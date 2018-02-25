import geopandas as gpd
from bokeh.io import save
from bokeh.models.sources import  ColumnDataSource
from bokeh.plotting import figure
from returnColumnDataSource import returnCDS
from flask import Flask, render_template, request
from bokeh.embed import components

filePath=r"geopandasData/IND_dest.shp"
filePathOverlayed=r"geopandasData/IND_water_lines_dcw_dest.shp"
outFile="./templates/LineStringOverlayed.html"
p = gpd.read_file(filePath)
q = gpd.read_file(filePathOverlayed)
bok = returnCDS(p)
bok1 = returnCDS(q)


fig = figure(title="first map with linestring",plot_width=900, plot_height=600)
fig.multi_line('x','y',source=bok,color='red', line_width=3)
fig.multi_line('x','y',source=bok1,color='blue',line_width=2)

app = Flask(__name__)

@app.route("/page0")
def roadRiver():
    script , div = components(fig)
    return render_template("page0.html",script=script,div=div,)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)