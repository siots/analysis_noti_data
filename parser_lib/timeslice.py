# -*- coding: utf-8 -*-

from parser_lib import stdtable

def timeslice_about_apprun(sorted_list):
    """
        :return type -- dict
        :key "time"+hour(int)
    """
    apprun = dict()
    for rows in sorted_list:
        if rows[stdtable.TYPE] == stdtable.TYPE_APPUSAGE:
            h = "time" + str(rows[stdtable.TIME_DATE].hour)
            if h in apprun:
                apprun[h] += 1
            else:
                apprun[h] = 1

    return apprun


def about_noti_run_interval(dict_run_all):
    app_list = dict()
    print "day : ", dict_run_all[0][3].day
    for rows in dict_run_all:
        h = "time" + str(rows[3].hour)
        if h in app_list:
            app_list[h].append(rows[1])
        else:
            app_list[h] = [rows[1]]
    for num in range(0,24):
        h = "time" + str(num)
        if h in app_list:
            print num, app_list[h]

    return app_list


def about_interval_with_appname(dict_run_all):
    app_list = dict()
    for rows in dict_run_all:
        if rows[0] in app_list:
            app_list[rows[0]].append([rows[3].hour, rows[1]])
        else:
            app_list[rows[0]] = [[rows[3].hour, rows[1]]]

    print app_list
    return app_list