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
    elif type(value) is unicode:
        csvfile.write(value.replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))
    else:
        csvfile.write(value.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ").replace("(", "[").replace(")", "]"))




def export_std_dict(std_dict, filepath, printable=False):
    with codecs.open(filepath, 'w', encoding="utf8") as csvfile:
        if printable :
            print "count screen on : ", std_dict[stdtable.f_dict_screen_on]
            print "count screen unlock : ", std_dict[stdtable.f_dict_screen_unlock]
            print "-- list of running app after unlock and noti --"

        csvfile.write("count screen (noti)-on , ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_on])
        csvfile.write("count screen (noti-on)-off , ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_off])
        csvfile.write("\n"+"count screen unlock immediately , ")
        write_csvfile(csvfile, std_dict[stdtable.f_dict_screen_unlock])
        csvfile.write("\n")

        # --------

        csvfile.write("\n")
        write_csvfile(csvfile, "노티 이후 전체 어플리케이션 리스트")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec), noti time, app usage time\n")

        list_of_dict = std_dict[stdtable.f_dict_list_run]
        sum_of_items = 0
        limit_sec = 60
        count_limit = 0
        for row in list_of_dict:
            if printable :
                print row[0], row[1]
            for col in row :
                write_csvfile(csvfile, col)
                csvfile.write(", ")
            csvfile.write("\n")
            sum_of_items += row[1]
            if row[1] < limit_sec:
                count_limit += 1

        if printable :
            print "total count : ", len(list_of_dict), "avg : ", 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict)
            print "count under ", limit_sec, "seconds : ", count_limit
            print "-- end --"
            print "-- list of running app all of after noti -- "

        csvfile.write("\n")
        csvfile.write("total count , ")
        write_csvfile(csvfile, len(list_of_dict))
        csvfile.write("\n")

        csvfile.write("avg , ")
        write_csvfile(csvfile, 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict))
        csvfile.write("\n")

        csvfile.write("count under ")
        write_csvfile(csvfile, limit_sec)
        csvfile.write(" seconds, ")
        write_csvfile(csvfile, count_limit)
        csvfile.write("\n")


        csvfile.write("\n")
        csvfile.write("\n")
        write_csvfile(csvfile, "노티 이후 실행된 앱 리스트(noti - unlock - run")
        csvfile.write("\n")
        csvfile.write("appname, interval(sec)\n")

        list_of_dict = std_dict[stdtable.f_dict_list_run_all]
        sum_of_items = 0
        limit_sec = 60
        count_limit = 0
        for row in list_of_dict:
            if printable :
                print row[0], row[1]

            write_csvfile(csvfile, row[0])
            csvfile.write(", ")
            write_csvfile(csvfile, row[1])
            csvfile.write("\n")

            sum_of_items += row[1]
            if row[1] < limit_sec:
                count_limit += 1

        if printable :
            print "total count : ", len(list_of_dict), "avg : ", 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict)
            print "count under ", limit_sec, "seconds : ", count_limit

        csvfile.write("\n")
        csvfile.write("total count , ")
        write_csvfile(csvfile, len(list_of_dict))
        csvfile.write("\n")
        csvfile.write("avg , ")
        write_csvfile(csvfile, 0 if len(list_of_dict) == 0 else sum_of_items/len(list_of_dict))
        csvfile.write("\n")
        csvfile.write("count under ")
        write_csvfile(csvfile, limit_sec)
        csvfile.write("seconds , ")
        write_csvfile(csvfile, count_limit)