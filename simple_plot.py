from bokeh.io import output_file, show
from bokeh.plotting import figure

f = figure(plot_width = 400, plot_height = 500, tools = 'pan, box_zoom')

output_file('my_plot.html')


x_axis = [1, 2, 3, 4, 5]
y_axis = [6, 7, 8, 9, 10]


f.line(x_axis, y_axis)

# Polishing plot, simple exaples of different polishing options
f.title.text = "My data"
f.title.text_color = "lime"
f.title.text_font = "times"
f.title.text_font_style = "bold"

f.xaxis.axis_label = "x_axis"
f.yaxis.axis_label = "y_axis"

show(f)