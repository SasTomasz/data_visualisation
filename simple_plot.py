from bokeh.io import output_file, show
from bokeh.plotting import figure

f = figure()

output_file('my_plot.html')


x_axis = [1, 2, 3, 4, 5]
y_axis = [6, 7, 8, 9, 10]


f.circle(x_axis, y_axis)
show(f)