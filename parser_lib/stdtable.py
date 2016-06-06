# -*- coding: utf-8 -*-

import dateformatter, applicationmanager
from operator import itemgetter

APP_NAME = 0
APP_NAME_TYPE = 1
SCREEN_STATUS = 2
NOTI_CONTENTS = 3
TIME_DATE = 4
TIME_SECONDS = 5
DURATION_SEC = 6
TYPE = 7

TYPE_APPUSAGE = "appusage"
TYPE_SAVER = "noti_saver"
TYPE_PRO = "noti_pro"
TYPE_EVENTLOG = "event"
TYPE_NOTI = "noti"

def std_table_app_usage(csv_list):
    std_table = []
    for num in range(1, len(csv_list)-1):
        row_list = []
        appname = csv_list[num][0]
        row_list.append(appname)
        row_list.append(appname+"["+TYPE_APPUSAGE+"]")
        row_list.append("")
        row_list.append("")
        # format_time = dateformatter.format_time_event_logger(csv_list[num][1].decode("utf-8"))
        format_time = dateformatter.format_time_another(csv_list[num][1].decode("utf-8"))
        # format_time = dateformatter.format_time_app_usage_eu(csv_list[num][1].decode("utf-8"))
        row_list.append(format_time)
        sec = dateformatter.formatdate_to_sec(format_time)
        row_list.append(sec)
        row_list.append(csv_list[num][3])
        row_list.append(TYPE_APPUSAGE)
        if(not applicationmanager.contains_filter(appname)):
            std_table.append(row_list)
    return std_table


def std_table_event_logger(csv_list):
    std_table = []
    for num in range(1, len(csv_list)-1):
        row_list = []
        row_list.append("")
        row_list.append("")
        row_list.append(applicationmanager.convert_eventlogger(csv_list[num][2]))
        row_list.append("")

        format_time = dateformatter.format_time_event_logger(csv_list[num][1].decode("utf-8"))

        # for daniel
        # format_time = dateformatter.format_time_event_logger_eu(csv_list[num][1].decode("utf-8"))


        row_list.append(format_time)
        row_list.append(dateformatter.formatdate_to_sec(format_time))
        row_list.append("")
        row_list.append(TYPE_EVENTLOG)
        if(len(row_list[2]) > 1):
            std_table.append(row_list)

    return std_table


def std_table_pro(csv_list):
    std_table = []
    for num in range(2, len(csv_list)):
        row_list = []
        appname = applicationmanager.convert_package2name(csv_list[num][1])
        row_list.append(appname)
        row_list.append(appname + "[noti_pro]")
        row_list.append("")
        row_list.append(csv_list[num][3].decode("utf-8"))
        format_time = dateformatter.format_time_hn(csv_list[num][4].decode("utf-8"))
        row_list.append(format_time)
        row_list.append(dateformatter.formatdate_to_sec(format_time))
        row_list.append("")
        row_list.append(TYPE_NOTI)
        if(not applicationmanager.contains_filter(appname)):
            std_table.append(row_list)
    return std_table

def std_table_saver(csv_list):
    std_table = []
    for num in range(2, len(csv_list)):
        row_list = []
        appname = csv_list[num][0]
        row_list.append(appname)
        row_list.append(appname + "[noti_saver]")
        row_list.append("")
        row_list.append(csv_list[num][5].decode("utf-8"))
        format_time = dateformatter.format_time_event_logger(csv_list[num][2].decode("utf-8"))
        # format_time = dateformatter.format_time_event_logger_eu(csv_list[num][2].decode("utf-8"))
        row_list.append(format_time)
        row_list.append(dateformatter.formatdate_to_sec(format_time))
        row_list.append("")
        row_list.append(TYPE_NOTI)
        if(not applicationmanager.contains_filter(appname)):
            std_table.append(row_list)
    return std_table

def get_standard_table(au, el, nh):
    std_table = []
    std_table.extend(au)
    std_table.extend(el)
    std_table.extend(nh)
    return std_table


def sort_std_table(std_table):
    std_table.sort(key=itemgetter(TIME_DATE))
    return std_table


def sort_by_appname(sorted_list):
    after_sort_list = []
    for appname in applicationmanager.whitelist_name():
        for row in sorted_list:
            if(row[APP_NAME] == appname or row[TYPE] == TYPE_EVENTLOG):
                after_sort_list.append(row)
    return after_sort_list

def slice_by_time(sorted_list, datetimes):
    timeslice_list = []
    for rows in sorted_list:
        if dateformatter.contains_day(rows[TIME_SECONDS],datetimes):
            timeslice_list.append(rows)
    return timeslice_list


def count_application(std_table):
    count_table = []
    for row in std_table:
        index = contains_count_table(row[APP_NAME], count_table)
        if index > -1:
            count_table[index][1] += 1
        else:
            count_table.append([row[APP_NAME], 1])
    return count_table


def contains_count_table(appname, count_table):
    for num in range(len(count_table)):
        if appname == count_table[num][0]:
            return num
    return -1

def count_between_run(sort_list):
    count_list = []
    for app in applicationmanager.whitelist_name():
        count = 0
        noti = False
        for rows in sort_list:
            if rows[APP_NAME] == app:
                if rows[TYPE] == TYPE_NOTI:
                    if not noti :
                        noti_time = rows[TIME_DATE]
                    noti = True
                    count += 1
                elif rows[TYPE] == TYPE_APPUSAGE:
                    if count > 0 and noti:
                        count_list.append([app, count, noti_time, rows[TIME_DATE], dateformatter.formatdate_to_sec(rows[TIME_DATE]) - dateformatter.formatdate_to_sec(noti_time)])
                    count = 0
                    noti = False
            elif len(rows[APP_NAME]) > 0:
                if count > 0 and noti:
                    count_list.append([app, count, noti_time, "", ""])
                    count = 0
                    noti = False
    return count_list



f_dict_screen_on = "screen_on"
f_dict_screen_off = "screen_off"
f_dict_screen_unlock = "screen_unlock"
f_dict_list_run = "list_run"
f_dict_list_run_on = "list_on"
f_dict_list_run_all = "list_all"


def contains_appname_index_countlist(appname_list, appname):
    if len(appname_list) == 0:
        return -1
    for num in range(len(appname_list)):
        if appname_list[num][0] == appname:
            return num
    return -1


def get_after_noti_data(std_table, usewhitelist=False):
    """
        :param
            @ std_table : need to standard table after sort by time.

        :return type -- dict
            @ f_dict_screen_on("screen_on") :
                count when screen turn on after App notification.\n
            @ f_dict_screen_unlock("screen_unlock") :
                count such as @countOn, But within any seconds like 60 sec.\n
            @ f_dict_list_run("list_run") :
                List of running app after notification and screen unlock.
                Contains App name, duration between notification and app resume.\n
            @ f_dict_list_run_all("list_all") :
                List of running app after notification.
                Contain such as notilist_need_run.

    """
    notilist_on = []
    countOn = 0
    countOff = 0
    flagOn = False
    flagOff = False

    notilist_unlock = []
    countOnUnlock = 0
    flagUnlock = False
    countOnUnlockImmediately = 0
    notilist_run_when_on = []

    app_count_list_run_on = []
    app_count_list_run_anyway = []
    app_count_list_run = []
    notilist_need_run = []
    notilist_need_run_anyway = []
    flagRun = False

    for rows in std_table:

        if rows[TYPE] == TYPE_NOTI and (not usewhitelist or applicationmanager.contains_whitelist(rows[APP_NAME])):
            notilist_on.append([rows[APP_NAME], rows[TIME_SECONDS]])
            notilist_unlock.append([rows[APP_NAME], rows[TIME_SECONDS]])
            # print rows[APP_NAME], applicationmanager.contains_whitelist(rows[APP_NAME]), not usewhitelist or applicationmanager.contains_whitelist(rows[APP_NAME])
            if contains_appname_index_countlist(notilist_need_run, rows[APP_NAME]) < 0:
                # print rows[APP_NAME], "------------------------"
                notilist_need_run.append([rows[APP_NAME], rows[TIME_SECONDS], rows[TIME_DATE], rows[NOTI_CONTENTS]])

            if contains_appname_index_countlist(notilist_need_run_anyway, rows[APP_NAME]) < 0:
                notilist_need_run_anyway.append([rows[APP_NAME], rows[TIME_SECONDS], rows[TIME_DATE], rows[NOTI_CONTENTS]])

            if contains_appname_index_countlist(notilist_run_when_on, rows[APP_NAME]) < 0:
                notilist_run_when_on.append([rows[APP_NAME], rows[TIME_SECONDS], rows[TIME_DATE], rows[NOTI_CONTENTS]])
                # print "in : ", rows[APP_NAME]

            #on
        elif rows[TYPE] == TYPE_EVENTLOG and rows[SCREEN_STATUS] == applicationmanager.eventlogger_table()[0]:
            flagOff = True
            flagOn = True
            del notilist_run_when_on[:]
            countOn += 1
            if(len(notilist_unlock) > 0):
                flagUnlock = True

            #off
        elif rows[TYPE] == TYPE_EVENTLOG and rows[SCREEN_STATUS] == applicationmanager.eventlogger_table()[1]:
            if (len(notilist_on) and flagOff):
                countOff += 1
            del notilist_on[:]
            flagOff = False
            flagOn = False

        #unlock
        elif rows[TYPE] == TYPE_EVENTLOG and rows[SCREEN_STATUS] == applicationmanager.eventlogger_table()[2] and len(notilist_unlock) > 0 and flagUnlock:
            countOnUnlock += 1
            # if flagUnlock:
            flagRun = True
            # print "flag run time", rows[TIME_DATE]
            flagUnlock = False
            if rows[TIME_SECONDS] - notilist_unlock[0][1] < 60:
                countOnUnlockImmediately += 1
                # print rows[TIME_DATE]

            del notilist_unlock[:]

        #app run
        elif rows[TYPE] == TYPE_APPUSAGE:
            index = contains_appname_index_countlist(notilist_need_run, rows[APP_NAME])
            # print "run at time : ", index, "|", rows[TIME_DATE], "|", rows[APP_NAME], contains_appname_index_countlist(notilist_need_run, rows[APP_NAME]) >= 0 and (not usewhitelist or applicationmanager.contains_whitelist(rows[APP_NAME]))
            if index >= 0:
                if flagRun:
                    app_count_list_run.append([notilist_need_run[index][0], rows[TIME_SECONDS] - notilist_need_run[index][1], notilist_need_run[index][2], rows[TIME_DATE], notilist_need_run[index][3], rows[DURATION_SEC]])
                    flagRun = False
                    del notilist_need_run[index]

            index = contains_appname_index_countlist(notilist_need_run_anyway, rows[APP_NAME])
            if index >= 0:
                app_count_list_run_anyway.append([notilist_need_run_anyway[index][0], rows[TIME_SECONDS] - notilist_need_run_anyway[index][1], notilist_need_run_anyway[index][2], rows[TIME_DATE], notilist_need_run_anyway[index][3], rows[DURATION_SEC]])
                del notilist_need_run_anyway[index]

            index = contains_appname_index_countlist(notilist_run_when_on, rows[APP_NAME])
            if index >= 0:
                if flagOn:
                    app_count_list_run_on.append([notilist_run_when_on[index][0], rows[TIME_SECONDS] - notilist_run_when_on[index][1], notilist_run_when_on[index][2], rows[TIME_DATE], notilist_run_when_on[index][3], rows[DURATION_SEC]])
                    del notilist_run_when_on[index]
                    flagOn = False


                    # elif rows[TYPE] == TYPE_APPUSAGE and rows[APP_NAME] == "카카오톡":
                    #     print "others : ", "|", rows[TIME_DATE], "|", rows[APP_NAME], "|", len(notilist_need_run)

    # for item in app_count_list_run:
    #     print item[0], item[1]
    # print "app count list run : ", len(app_count_list_run)
    # for item in app_count_list_run_anyway:
    #     print item[0], item[1]
    # print "app count list run : ", len(app_count_list_run_anyway)

    count_dict = dict()
    count_dict[f_dict_screen_on] = countOn
    count_dict[f_dict_screen_off] = countOff
    count_dict[f_dict_screen_unlock] = countOnUnlockImmediately
    count_dict[f_dict_list_run] = app_count_list_run
    count_dict[f_dict_list_run_on] = app_count_list_run_on
    count_dict[f_dict_list_run_all] = app_count_list_run_anyway

    # print countOnUnlockImmediately
    return count_dict