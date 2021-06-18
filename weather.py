from bokeh.models.sources import ColumnDataSource
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.layouts import row
from bokeh.models import CrosshairTool, formatters
from bokeh.models import HoverTool

df_Ed = pd.read_csv("Edmonton1.csv")
df_Ed.index += 1
date = pd.to_datetime(df_Ed['Date/Time']).tolist()
mean_temp = df_Ed["Mean Temp (°C)"].tolist()
high_temp = df_Ed["Max Temp (°C)"].tolist()
low_temp = df_Ed["Min Temp (°C)"].tolist()

Edm = figure(title='Edmonton\'s Low, High, and Mean Temperatures in 2021', x_axis_label='Date', y_axis_label='Temperature', x_axis_type='datetime')
Edm.line(x=date, y=mean_temp, color="#000000", legend_label='Mean')
Edm.line(x=date, y=high_temp, color="#2785db", legend_label='High')
Edm.line(x=date, y=low_temp, color="#d83939", legend_label='Low')

df_Van = pd.read_csv("Vancouver.csv")
df_Van.index += 1
# date1 = pd.to_datetime(df_Van['Date/Time']).tolist()
mean_temp1 = df_Van["Mean Temp (°C)"].tolist()
high_temp1 = df_Van["Max Temp (°C)"].tolist()
low_temp1 = df_Van["Min Temp (°C)"].tolist()
Van = figure(title='Vancouver\'s Low, High, and Mean Temperatures in 2021', x_axis_label='Date', y_axis_label='Temperature', x_axis_type='datetime')
Van.line(x=date, y=mean_temp1, color="#000000", legend_label='Mean')
Van.line(x=date, y=high_temp1, color="#2785db", legend_label='High')
Van.line(x=date, y=low_temp1, color="#d83939", legend_label='Low')

all_locations = figure(title='Edmonton and Vancouver\'s Mean Temperatures', x_axis_label='Date', y_axis_label='Temperature', x_axis_type='datetime')

temps = {'Vancouver': mean_temp1,
        'Edmonton': mean_temp}
colours = ["#000000", "#2785db"]

for temp, location, color in zip(temps.values(), temps.keys(), colours):
    size = len(temp)
    locations = [location for i in range(size)]
    source = ColumnDataSource(data={
        'Date': date,
        'Temperature': temp,
        'Location': locations
    })
    all_locations.line(x='Date', y='Temperature', color=color, legend_label = location, source = source)

all_locations.legend.location = 'top_left'

all_locations.add_tools(CrosshairTool())
all_locations.legend.click_policy = 'hide'
all_locations.add_tools(HoverTool(
    tooltips=[
        ('Location', '@Location'),
        ('Temperature', '@Temperature'),
        ('Date', '@Date{%F}')
    ],
    formatters={
        '@Date': 'datetime'
    }))

show(row(Edm, Van))
show(all_locations)