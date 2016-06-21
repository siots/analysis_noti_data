# -*- coding: utf-8 -*-

from parser_lib import table_manager, csvhelper, stdtable, applicationmanager, dateformatter, timeslice, chartmanager
import codecs
import datetime

def testcase():
    # table_manager.print_table(stdtable.sort_by_appname(sort_std))
    # table_manager.print_table(sort_std)
    # table_manager.print_table(sort_std)

    # table_manager.print_table(stdtable.count_application(sort_std))
    pass


def exportCountBetweenRun(sorted_std_list, export_path, printable=False):

    count_list = stdtable.count_between_run(sorted_std_list)
    if printable:
        table_manager.print_table(count_list)
    csvhelper.export(count_list, export_path+"noti_count.csv", 'app name, count, noti_start_time, run_time, gap')

def getRawDataSet(data_path):
    csv_list1 = csvhelper.csv_parser(data_path+"AppUsage.csv")
    csv_list2 = csvhelper.csv_parser(data_path+"event_logger.csv")
    csv_list3 = csvhelper.csv_parser(data_path+"saver.csv")
    return csv_list1, csv_list2, csv_list3

def stdTableSort(stdTable, date):
    sort_std = stdtable.sort_std_table(stdTable)
    sort_std = stdtable.slice_by_time(sort_std, date)

    # sort_std = stdtable.sort_by_appname(sort_std)
    return sort_std



def exportDataSet(date, sort_std, export_path):
    csvhelper.export(sort_std, export_path+"data.csv", 'app name, app name[type], screen_status, noti_title, noti_contents, time_date, time_seconds, duration_sec, type')
    sort_std = stdtable.sort_by_appname(sort_std)
    exportCountBetweenRun(sort_std, export_path)

def get_standard_table(path, date):
    csv_list1, csv_list2, csv_list3 = getRawDataSet(path)
    au = stdtable.std_table_app_usage(csv_list1)
    saver = stdtable.std_table_saver(csv_list3)
    raw_standard_table = stdtable.get_standard_table(au, stdtable.std_table_event_logger(csv_list2), saver)
    sorted_table_by_date = stdTableSort(raw_standard_table, date)
    append_style_standard_table = stdtable.append_row_style(sorted_table_by_date)
    append_style_standard_table = stdtable.revision_is_sleep(append_style_standard_table)

    return append_style_standard_table

def export_file():
    dir = "jimyo/"
    # dir = "june/"
    # dir = "sss/"
    sday = 20
    eday = 24

    # dir = "mom/"
    # sday = 15
    # eday = 18
    # dir = "daniel/"
    # sday = 18
    # eday = 21

    path = "./data/"+dir
    for day in range(sday, eday):
        date = "2016-05-"+str(day)
        export_path = "./export/"+dir+date+"/"
        std_table = get_standard_table(path, date)

        if day == 22:
            # get_ad(saver)
            ds = timeslice.timeslice_about_apprun(std_table)
            # for rows in s:
            #     for cols in rows:
            #         print cols, "|",
            #     print
            # csvhelper.export(s, "./export/before.csv", 'app name, app name[type], screen_status, noti_title, noti_contents, time_date, time_seconds, duration_sec, type, status, issleep')
        # else :
        #     return
        # print len(sorted_table)
        # #
        # # # I don't wanna export this function. not yet.
        # applicationmanager.getDefaultAppInfo(csv_list1, csv_list2, csv_list3,export_path+"common_app_list.txt")
        # exportDataSet(date, sorted_table, export_path)
        #
            noti_analytics_dict = stdtable.get_after_noti_data(std_table, usesleep=True)
            # ds = timeslice.about_noti_run_interval(noti_analytics_dict[stdtable.f_dict_list_run_all])
            # chartmanager.timeslice(ds)
            dd = timeslice.about_interval_with_appname(noti_analytics_dict[stdtable.f_dict_list_run_all])
            for i in dd:
                print i, dd[i]
            chartmanager.interval_by_appname(dd)
        # csvhelper.export_std_dict(d, export_path+"analysis.csv")

def get_ad(std_saver):
    app_list = []
    for row in std_saver:
        if "광고".decode("utf-8") in row[stdtable.NOTI_CONTENTS]:
            index = stdtable.contains_count_table(row[stdtable.APP_NAME], app_list)
            if index >= 0:
                app_list[index][1].append(row)
            else:
                app_list.append((row[stdtable.APP_NAME], [row]))
    for row in app_list:
        for col in row:
            if type(col) == list:
                for contents_row in col:
                    for contents in contents_row:
                        print contents
                    print "---------------------------------"
            else:
                print col
        print "\n\n==============================================="


def sort_test():
    stdlist = []
    #
    # date = datetime.datetime(2016, 6, 5, 22, 30, 30)
    # stdlist.append(["카카오톡", "카카오톡", "", "hi", "hihi", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_NOTI])
    # date = datetime.datetime(2016, 6, 5, 22, 31, 30)
    # stdlist.append(["", "", stdtable.f_dict_screen_off, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    # date = datetime.datetime(2016, 6, 5, 22, 32, 30)
    # stdlist.append(["", "", stdtable.f_dict_screen_on, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    # date = datetime.datetime(2016, 6, 5, 22, 33, 30)
    # stdlist.append(["", "", stdtable.f_dict_screen_unlock, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    # date = datetime.datetime(2016, 6, 5, 22, 34, 30)
    # stdlist.append(["카카오톡", "카카오톡", "", "", "", date, dateformatter.formatdate_to_sec(date), 40, stdtable.TYPE_APPUSAGE])
    #
    # date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    # stdlist.append(["카카오톡", "카카오톡", "", "hi", "hihi", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_NOTI])
    # date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    # stdlist.append(["", "", stdtable.f_dict_screen_unlock, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    # date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    # stdlist.append(["카카오톡", "카카오톡", "", "", "", date, dateformatter.formatdate_to_sec(date), 40, stdtable.TYPE_APPUSAGE])

    date = datetime.datetime(2016, 6, 5, 22, 30, 30)
    stdlist.append(["카카오톡", "카카오톡", "", "hi", "hihi", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_NOTI])
    date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    stdlist.append(["카카오톡", "카카오톡", "", "hi", "hihi", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_NOTI])
    date = datetime.datetime(2016, 6, 5, 22, 34, 30)
    stdlist.append(["카카오톡", "카카오톡", "", "", "", date, dateformatter.formatdate_to_sec(date), 40, stdtable.TYPE_APPUSAGE])
    date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    stdlist.append(["카카오톡", "카카오톡", "", "", "", date, dateformatter.formatdate_to_sec(date), 40, stdtable.TYPE_APPUSAGE])
    date = datetime.datetime(2016, 6, 5, 22, 35, 30)
    stdlist.append(["", "", stdtable.f_dict_screen_unlock, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    date = datetime.datetime(2016, 6, 5, 22, 31, 30)
    stdlist.append(["", "", stdtable.f_dict_screen_off, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    date = datetime.datetime(2016, 6, 5, 22, 32, 30)
    stdlist.append(["", "", stdtable.f_dict_screen_on, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])
    date = datetime.datetime(2016, 6, 5, 22, 33, 30)
    stdlist.append(["", "", stdtable.f_dict_screen_unlock, "", "", date, dateformatter.formatdate_to_sec(date), "", stdtable.TYPE_EVENTLOG])



    sorted = stdTableSort(stdlist, "2016-06-05")

    for row in sorted:
        for col in row:
            if col:
                print col, "\t|",
            else:
                print "\t", "|",
        print

if __name__=="__main__":
    # test()
    # print convert_eventlogger("Screen Unlocked")
    # print contains_filter_package("com.buzzpia.aqua.launcher")
    export_file()
    # csvhelper.csv_parser("./data/6.1/test.csv", True)
    # time_test()
    # test2()
    # print dateformatter.format_time_event_logger(u"2016. 5. 21. 오전 00:27:02")
    # print dateformatter.format_time_hn(u" 2016-5-21 0:27:02")
    # sort_test()




def time_test():
    path = "./data/6.1/"
    date = "2016-06-01"
    csv_list1 = csvhelper.csv_parser(path+"test.csv")
    csv_list2 = csvhelper.csv_parser(path+"AppUsage_test.csv")
    std1 = stdtable.std_table_saver(csv_list1)
    std = stdtable.std_table_app_usage(csv_list2)
    # std = stdtable.get_standard_table(std2, [], std1)

    sort_std = stdtable.sort_std_table(std)
    sort_std = stdtable.slice_by_time(sort_std, date)
    sort_std = stdtable.sort_by_appname(sort_std)

    table_manager.print_table(sort_std)

    # exportCountBetweenRun(sort_std)


def test1():
    csv_list1 = csvhelper.csv_parser("./data/AppUsage.csv")
    std = stdtable.std_table_app_usage(csv_list1)
    table_manager.print_table(std)
    table_manager.print_table(stdtable.count_application(std))
    # csvhelper.export(std, "std.csv", 'app name, app name[type], screen_status, time_date, time_seconds, duration_sec, type')

def test2():
    csv_list = csvhelper.csv_parser("./data/6.1/saver.csv")
    table_manager.dupllicate_tuple_saver(csv_list, True)
    # table_manager.print_table(stdtable.std_table_saver(csv_list))

def test():
    csv_list1 = csvhelper.csv_parser("./data/AppUsage.csv")
    # dupllicate_tuple_app_usage(csv_list1)
    # print format_time_app_usage(csv_list1[5][1])
    # print_table(std_table_app_usage(csv_list1))

    print '-----------------------------------------'
    csv_list2 = csvhelper.csv_parser("./data/event_logger.csv")
    # dupllicate_tuple_logger(csv_list2)
    # print format_time_event_logger(csv_list2[5][1])
    # print_table(std_table_event_logger(csv_list2))


    csv_list3 = csvhelper.csv_parser("./data/sss2.xml.csv")
    # dupllicate_tuple_pro(csv_list3)
    # print format_time_hn(csv_list3[5][4])
    # print replace_table()
    cc= stdtable.std_table_pro(csv_list3)
    # print_table(cc)

    std = stdtable.get_standard_table(stdtable.std_table_app_usage(csv_list1), stdtable.std_table_event_logger(csv_list2),stdtable.std_table_pro(csv_list3))
    # print_std_table(std)
    sort_std = stdtable.sort_std_table(std)
    table_manager.print_table(sort_std)
    # csvhelper.export(sort_std, "hello2.csv", 'app name, app name[type], screen_status, time_date, time_seconds, duration_sec, type')

    # print csv_list
    print "--------------"
