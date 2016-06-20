# -*- coding: utf-8 -*-

import time
from datetime import datetime
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

def about_noti_run_interval(sorted_list):
    app_list = dict()
    print "day : ", sorted_list[0][3].day
    for rows in sorted_list:
        h = "time" + str(rows[3].hour)
        if h in app_list:
            app_list[h].append(rows[1])
        else:
            app_list[h] = [rows[1]]
    for num in range(0,24):
        h = "time" + str(num)
        if h in app_list:
            print num, app_list[h]
