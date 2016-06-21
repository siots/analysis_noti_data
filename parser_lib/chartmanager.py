from plotly import plotly, tools
import key
import plotly.plotly as py
from plotly.graph_objs import *
import stdtable

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

def interval_by_hour(timeslice_dict, chartname="interval_by_hour"):
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
                mode="markers",
                name=timeh
            )
            datas.append(trace)
    data = Data(datas)

    py.plot(data, filename=chartname)

def interval_by_appname(dict_by_appname, chartname="interval_by_appname"):
    datas = []
    for name in dict_by_appname:
        x = []
        y = []
        print name
        for rows in dict_by_appname[name]:
            x.append(rows[0])
            y.append(rows[1])
        trace = Scatter(
            x=x,
            y=y,
            mode="markers",
            name=name
        )
        datas.append(trace)
    data = Data(datas)

    py.plot(data, filename=chartname)


def interval_count_until_noti(list_run, chartname="interval_count_until_noti"):
    datas = []

    dict_by_appname = dict()
    for rows in list_run:
        name = rows[stdtable.DICT_APPNAME]
        if name in dict_by_appname:
            dict_by_appname[name].append([rows[stdtable.DICT_INTERVAL], rows[stdtable.DICT_NOTI_COUNT]])
        else:
            dict_by_appname[name] = [[rows[stdtable.DICT_INTERVAL], rows[stdtable.DICT_NOTI_COUNT]]]

    for name in dict_by_appname:
        x = []
        y = []
        print name, dict_by_appname[name]
        for rows in dict_by_appname[name]:
            x.append(rows[1])
            y.append(rows[0])
        trace = Scatter(
            x=x,
            y=y,
            mode="markers",
            name=name
        )
        datas.append(trace)
    data = Data(datas)

    py.plot(data, filename=chartname)


def interval_duration(list_run, chartname="interval_duration"):
    datas = []

    dict_by_appname = dict()
    for rows in list_run:
        name = rows[stdtable.DICT_APPNAME]
        if name in dict_by_appname:
            dict_by_appname[name].append([rows[stdtable.DICT_INTERVAL], rows[stdtable.DICT_DURATION]])
        else:
            dict_by_appname[name] = [[rows[stdtable.DICT_INTERVAL], rows[stdtable.DICT_DURATION]]]

    for name in dict_by_appname:
        x = []
        y = []
        print name, dict_by_appname[name]
        for rows in dict_by_appname[name]:
            x.append(rows[0])
            y.append(rows[1])
        trace = Scatter(
            x=x,
            y=y,
            mode="markers",
            name=name
        )
        datas.append(trace)
    data = Data(datas)

    py.plot(data, filename=chartname)


# need separate each person
def noti_run_count(count_list, chartname="noti_run_count"):
    datas=[]

    for name in count_list:
        print name, count_list[name], count_list[name][0], count_list[name][1]
        trace = Scatter(
            x=count_list[name][0],
            y=count_list[name][1],
            mode="markers",
            name=name
        )
        datas.append(trace)
    data = Data(datas)

    py.plot(data, filename=chartname)
