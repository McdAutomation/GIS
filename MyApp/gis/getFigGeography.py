import geopandas as gpd
from bokeh.io import save
from bokeh.models.sources import  ColumnDataSource
from bokeh.models import Label
from bokeh.plotting import figure
from MyApp.gis.conversions.returnColumnDataSource import returnCDS
from flask import Flask, render_template, request
from bokeh.embed import components
from MyApp.gis.conversions.returnPolygonBokeh import returnPDS
from geopandas.tools import geocode
from geopandas.tools import geocode
from MyApp.gis.conversions.returnCircleBokeh import returnCircle
from bokeh.models import HoverTool, TapTool, OpenURL
filePath=r"./data/india_ds.shp"
key = "AIzaSyBt-PMS8TXJ4v4GzcitUu0l_4ckFKoyjHE"

outFile="./templates/GeoCoding.html"
p = gpd.read_file(filePath)

bok = returnPDS(p)

address = "pune"
cir = geocode(address,api_key=key)
cir = returnCircle(cir)

figGeography= figure(title="first map with geocoding polygon",plot_width=800, plot_height=800)
lineGlyph=figGeography.multi_line('x','y',source=bok,color='red', line_width=3,legend='MultiLine')
circleGlyph=figGeography.circle('x','y',source=cir, size=5, color='black',legend='circle')

citation = Label(x=10, y=700, x_units='screen', y_units='screen',
                 text='Sample text box', render_mode='css',
                 border_line_color='red', border_line_alpha=1.0,
                 background_fill_color='yellow', background_fill_alpha=1.0)
figGeography.add_layout(citation)


def create_hover_tool_india():
    """Generates the HTML for the Bokeh's hover data tool on our graph."""
    hover_html  = """
      <div>
        <span class="hover-tooltip">State: @STATE
      </div>
        """
    return HoverTool(renderers=[lineGlyph],tooltips=hover_html)
def create_hover_tool_address():
    """Generates the HTML for the Bokeh's hover data tool on our graph."""
    hover_html  = """
      <div>
        <span class="hover-tooltip">Address: @address
      </div>
        """
    return HoverTool(renderers=[circleGlyph],tooltips=hover_html)

url = "http://www.colors.commutercreative.com/"
taptool = TapTool(renderers=[circleGlyph])
taptool.callback = OpenURL(url=url)

figGeography.add_tools(create_hover_tool_india())
figGeography.add_tools(create_hover_tool_address())
figGeography.add_tools(taptool)
