# -*- coding: utf-8 -*-

from parser_lib import table_manager, csvhelper, stdtable, applicationmanager, dateformatter
import codecs

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
    sort_std = stdtable.sort_by_appname(sort_std)
    exportCountBetweenRun(sort_std, export_path)
    csvhelper.export(sort_std, export_path+"data.csv", 'app name, app name[type], screen_status, noti_contents, time_date, time_seconds, duration_sec, type')


def main():
    dir = "jimyo/"
    # dir = "june/"
    dir = "sss/"
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
        csv_list1, csv_list2, csv_list3 = getRawDataSet(path)
        au = stdtable.std_table_app_usage(csv_list1)
        std = stdtable.get_standard_table(au, stdtable.std_table_event_logger(csv_list2), stdtable.std_table_saver(csv_list3))
        sorted_table = stdTableSort(std, date)

        # I don't wanna export this function. not yet.
        applicationmanager.getDefaultAppInfo(csv_list1, csv_list2, csv_list3,export_path+"common_app_list.txt")
        exportDataSet(date, sorted_table, export_path)

        d = stdtable.get_after_noti_data(sorted_table)
        csvhelper.export_std_dict(d, export_path+"analysis.csv")

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

if __name__=="__main__":
    # test()
    # print convert_eventlogger("Screen Unlocked")
    # print contains_filter_package("com.buzzpia.aqua.launcher")
    main()
    # csvhelper.csv_parser("./data/6.1/test.csv", True)
    # time_test()
    # test2()
    # print dateformatter.format_time_event_logger(u"2016. 5. 21. 오전 00:27:02")
    # print dateformatter.format_time_hn(u" 2016-5-21 0:27:02")





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
