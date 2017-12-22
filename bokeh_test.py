# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:49:50 2017

@author: rbarnes
"""
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox,column
from bokeh.models.widgets import RadioGroup
from bokeh.plotting import figure, curdoc
import numpy as np
import time
x=[1,2,3,4]
y=[[1,2,3,4],[1,-2,3,-4],[1,4,9,16]]
p = figure(x_range=[1,4], y_range=(0,20))
line1 = p.line(x,y[0],name='line1')
line2 = p.line(x,y[1],name='line2')
line3 = []
for i in range(100):
    line3.append(p.line(x,[obj**2+np.random.normal() for obj in x],name='line3'))
line1.glyph.line_alpha=0
line2.glyph.line_alpha=0
for line in line3:
    line.glyph.line_alpha=0
def my_radio_handler(new):
    line1.glyph.line_alpha=0
    line2.glyph.line_alpha=0
    for line in line3:

        line.glyph.line_alpha=0
    if new == 0:
        line1.glyph.line_alpha=100
    elif new == 1:
        line2.glyph.line_alpha=100
    elif new == 2:
        for line in line3:
            time.sleep(0.1)
            line.glyph.line_alpha=1
    else:
        print('Error')

radio_group = RadioGroup(
    labels=["Option 1", "Option 2", "Option 3"], active=0)
radio_group.on_click(my_radio_handler)

curdoc().add_root(column(widgetbox(radio_group),p))