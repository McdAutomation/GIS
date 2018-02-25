import geopandas as gpd
from bokeh.io import save
from bokeh.models.sources import  ColumnDataSource
from bokeh.models import Label
from bokeh.plotting import figure
from returnColumnDataSource import returnCDS
from flask import Flask, render_template, request
from bokeh.embed import components
from returnPolygonBokeh import returnPDS
from geopandas.tools import geocode
from geopandas.tools import geocode
from returnCircleBokeh import returnCircle
filePath=r"geopandasData/india_ds.shp"
key = "AIzaSyBt-PMS8TXJ4v4GzcitUu0l_4ckFKoyjHE"

#filePathOverlayed=r"geopandasData/india_ds_dest.shp"
outFile="./templates/GeoCoding.html"
p = gpd.read_file(filePath)
#q = gpd.read_file(filePathOverlayed)
bok = returnPDS(p)
#bok1 = returnPDS(q)

address = "pune"
cir = geocode(address,api_key=key)
cir = returnCircle(cir)

fig = figure(title="first map with geocoding polygon",plot_width=800, plot_height=800)
fig.multi_line('x','y',source=bok,color='red', line_width=3,legend='MultiLine')
#fig.multi_line('x','y',source=bok1,color='blue',line_width=2)
fig.circle('x','y',source=cir, size=5, color='black',legend='circle')

citation = Label(x=10, y=700, x_units='screen', y_units='screen',
                 text='Sample text box', render_mode='css',
                 border_line_color='red', border_line_alpha=1.0,
                 background_fill_color='yellow', background_fill_alpha=1.0)
fig.add_layout(citation)
app = Flask(__name__)

@app.route("/geo0")
def roadRiver():
    script , div = components(fig)
    return render_template("page0.html",script=script,div=div,)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)