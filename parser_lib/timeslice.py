# -*- coding: utf-8 -*-

from parser_lib import stdtable

# run count by hours
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

# interval by hours
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
        if rows[0] in app_list and rows[1] <= 7200:
            app_list[rows[0]].append([rows[3].hour, rows[1]])
        elif rows[1] <= 7200:
            app_list[rows[0]] = [[rows[3].hour, rows[1]]]

    return app_list


# def noticount_runcount_by_appname(sorted_list):
#     app_list = dict()
#     for rows in sorted_list:
#         if rows[stdtable.TYPE] == stdtable.TYPE_NOTI


def noti_run_count_with_user(sorted_list, username):

    count_list = dict()
    for rows in sorted_list:
        if rows[stdtable.TYPE] == stdtable.TYPE_NOTI:
            name = rows[stdtable.APP_NAME]+"-"+username
            if name in count_list:
                count_list[name][0] += 1
            else:
                count_list[name] = [1, 0]

        elif rows[stdtable.TYPE] == stdtable.TYPE_APPUSAGE:
            name = rows[stdtable.APP_NAME]+"-"+username
            if name in count_list:
                count_list[name][1] += 1
            else:
                count_list[name] = [0, 1]

    return count_list
