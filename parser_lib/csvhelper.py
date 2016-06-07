#-*- coding: utf-8 -*-
import csv,codecs
import stdtable
from datetime import datetime

def csv_parser(filename, printable=False):
    csv_list = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_list=[]
            for col in row:
                if printable :
                    if type(col) is unicode:
                        print col.decode('utf-8').encode('utf-8'), '|',
                    elif type(col) is str:
                        print col, '|',
                row_list.append(col.decode('utf-8').encode('utf-8'))
            if printable :
                print
            csv_list.append(row_list)
    return csv_list

def export(std_table, filepath, csv_format):
    with codecs.open(filepath, 'w', encoding="utf8") as csvfile:
        csvfile.write(csv_format+'\n')
        for row in std_table:
            for col in row:
                # print col, type(col), type(datetime.now()), float
                if type(col) is type(datetime.now()):
                    csvfile.write(str(col.strftime('%Y-%m-%d %H:%M:%S')))
                elif type(col) is float or type(col) is int:
                    csvfile.write(str(col))
                elif type(col) is unicode:
                    csvfile.write(col.replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))
                else:
                    csvfile.write(col.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))
                csvfile.write(", ")
            csvfile.write('\n')

def write_csvfile(csvfile, value):
    if type(value) is float or type(value) is int:
        csvfile.write(str(value))
    elif type(value) is type(datetime.now()):
        csvfile.write(str(value.strftime('%Y-%m-%d %H:%M:%S')))
    elif type(value) is unicode:
        csvfile.write(value.replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))
    else:
        csvfile.write(value.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))

def export_rank(std_table, filepath, printable = False):
    noti_rank_list = []
    duration_rank_list = []
    noti_response_rank_list = []

    for row in stdtable:
        pass
    with codecs.open(filepath, 'w', encoding="utf8") as csvfile:
        csvfile.write()


def export_std_dict(std_dict, filepath, printable=False):
    with codecs.open(filepath, 'w', encoding="utf8") as csvfile:
        if printable :
            print "count screen on : ", std_dict[stdtable.f_dict_screen_on]
            print "count screen unlock : ", std_dict[stdtable.f_dict_screen_unlock]
            print "-- list of running app after unlock and noti --"

        write_csvfile(csvfile, "0. 일일 unlock 횟수")
        csvfile.write(", ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_unlock])
        csvfile.write("\n")
        write_csvfile(csvfile, "1. 총 노티 갯수")
        csvfile.write(", ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_count_noti])
        csvfile.write("\n")
        write_csvfile(csvfile, "2. noti - screen on : 노티로 화면이 켜진 횟수")
        csvfile.write(", ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_on])
        csvfile.write("\n")
        write_csvfile(csvfile, "3. noti - screen on - off: 노티 온 후 즉시 확인 못한 횟수")
        csvfile.write(", ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_off])
        csvfile.write("\n")

        # --------

        list_of_dict = std_dict[stdtable.f_dict_list_run]
        sum_of_items = 0
        limit_sec = 60
        count_limit = 0
        count_within_limit_list = []
        count_over_limit_list = []
        sum_of_items_under = 0
        sum_of_items_over = 0
        for row in list_of_dict:
            sum_of_items += row[1]
            if row[1] <= limit_sec:
                count_limit += 1
                count_within_limit_list.append(row)
                sum_of_items_under += row[1]
            else:
                count_over_limit_list.append(row)
                sum_of_items_over += row[1]

        if printable:
            print "1)total count : ", len(list_of_dict), "avg : ", 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict)
            print "count under ", limit_sec, "seconds : ", count_limit
            print "-- end --"
            print "-- list of running app all of after noti -- "



        csvfile.write("\n")
        write_csvfile(csvfile, "4. noti - unlock - run@under 60s (screen off) : off시, 노티 온 후 즉시(60s) 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_within_limit_list) == 0 else sum_of_items_under/len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")
        for row in count_within_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            if printable:
                print "\n"
            csvfile.write("\n")


        csvfile.write("\n")
        write_csvfile(csvfile, "5. noti - unlock - run@over 60s (screen off) : off시, 노티 온 후 나중에 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_over_limit_list))
        csvfile.write("\n")
        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_over_limit_list) == 0 else sum_of_items_over/len(count_over_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")
        sum_of_items = 0
        for row in count_over_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            sum_of_items += row[1]
            if printable:
                print "\n"
            csvfile.write("\n")

        list_of_dict = std_dict[stdtable.f_dict_list_run_on]
        sum_of_items = 0
        limit_sec = 60
        count_limit = 0
        count_within_limit_list = []
        count_over_limit_list = []
        sum_of_items_under = 0
        sum_of_items_over = 0
        for row in list_of_dict:
            sum_of_items += row[1]
            if row[1] <= limit_sec:
                count_limit += 1
                count_within_limit_list.append(row)
                sum_of_items_under += row[1]
            else:
                count_over_limit_list.append(row)
                sum_of_items_over += row[1]

        if printable :
            print "1)total count : ", len(list_of_dict), "avg : ", 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict)
            print "count under ", limit_sec, "seconds : ", count_limit

        csvfile.write("\n")
        csvfile.write("\n")
        write_csvfile(csvfile, "6. noti - run@under 60s (screen on) : on시, 노티 온 후 즉시 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_within_limit_list) == 0 else sum_of_items_under/len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")

        for row in count_within_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            if printable:
                print "\n"
            csvfile.write("\n")



        csvfile.write("\n")
        write_csvfile(csvfile, "7. noti - run@over 60s (screen on) : on시, 노티 온 후 나중에 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_over_limit_list))
        csvfile.write("\n")
        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_over_limit_list) == 0 else sum_of_items_over/len(count_over_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")
        sum_of_items = 0
        for row in count_over_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            sum_of_items += row[1]
            if printable:
                print "\n"
            csvfile.write("\n")

        list_of_dict = std_dict[stdtable.f_dict_list_run_all]
        sum_of_items = 0
        limit_sec = 60
        count_limit = 0
        count_within_limit_list = []
        count_over_limit_list = []
        sum_of_items_under = 0
        sum_of_items_over = 0
        for row in list_of_dict:
            sum_of_items += row[1]
            if row[1] <= limit_sec:
                count_limit += 1
                count_within_limit_list.append(row)
                sum_of_items_under += row[1]
            else:
                count_over_limit_list.append(row)
                sum_of_items_over += row[1]

        if printable :
            print "1)total count : ", len(list_of_dict), "avg : ", 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict)
            print "count under ", limit_sec, "seconds : ", count_limit

        csvfile.write("\n")
        csvfile.write("\n")
        write_csvfile(csvfile, "8. noti-run@under 60s (screen on, off 전체) : on/off시, 노티 온 후 즉시 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_within_limit_list) == 0 else sum_of_items_under/len(count_within_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")

        for row in count_within_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            if printable:
                print "\n"
            csvfile.write("\n")


        csvfile.write("\n")
        write_csvfile(csvfile, "9. noti-run@over 60s (screen on, off 전체) : on/off시, 노티 온 후 나중에 앱 실행한 횟수")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("1)total count , ")
        write_csvfile(csvfile, len(count_over_limit_list))
        csvfile.write("\n")

        csvfile.write("2)interval avg , ")
        write_csvfile(csvfile, 0 if len(count_over_limit_list) == 0 else sum_of_items_over/len(count_over_limit_list))
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time, title, contents, app use durations\n")

        for row in count_over_limit_list:
            for col in row:
                if printable:
                    print col,
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            if printable:
                print "\n"
            csvfile.write("\n")