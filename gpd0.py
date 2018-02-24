import geopandas as gpd
from bokeh.io import save
from bokeh.models.sources import  ColumnDataSource
from bokeh.plotting import figure
from returnColumnDataSource import returnCDS

filePath=r"geopandasData/IND_dest.shp"
filePathOverlayed=r"geopandasData/IND_water_lines_dcw_dest.shp"
outFile="./templates/LineStringOverlayed.html"
p = gpd.read_file(filePath)
q = gpd.read_file(filePathOverlayed)
bok = returnCDS(p)
bok1 = returnCDS(q)


fig = figure(title="first map with linestring")
fig.multi_line('x','y',source=bok,color='red', line_width=3)
fig.multi_line('x','y',source=bok1,color='blue',line_width=2)



save(fig,outFile)