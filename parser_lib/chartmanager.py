from plotly import plotly, tools
import key
import plotly.plotly as py
from plotly.graph_objs import *

tools.set_credentials_file(username=key.username, api_key=key.apikey)

def tutorial():

    trace0 = Scatter(
        x=[1, 2, 3, 3],
        y=[10, 15, 13, 17],
        mode="markers"
    )
    trace1 = Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9],
        mode="markers"
    )
    data = Data([trace0, trace1])

    py.plot(data, filename='test')

def timeslice(timeslice_dict):
    datas = []
    for num in range(0, 24):
        h = str(num)
        timeh = "time"+h
        if timeh in timeslice_dict:
            x = []
            print "t", h, timeslice_dict[timeh]
            for i in timeslice_dict[timeh]:
                x.append(h)
            print x
            trace = Scatter(
                x=x,
                y=timeslice_dict[timeh],
                mode="markers"
            )
            datas.append(trace)
    data = Data(datas)

    py.plot(data, filename='test')