#-*- coding: utf-8 -*-


def print_table(table):
    for row in table:
        for col in row:
            print col, "|",
        print


def dupllicate_tuple_app_usage(csv_list, printable=False):
    dup = []
    for num in range(1, len(csv_list)-1):
        if(not(csv_list[num][0] in dup)):
            dup.append(csv_list[num][0])
    if printable:
        print "App Usage-------------------"
        for item in dup:
            print item
    return dup


def dupllicate_tuple_saver(csv_list, printable=False):
    dup = []
    for num in range(1, len(csv_list)-1):
        if(not([csv_list[num][0],csv_list[num][1]] in dup)):
            dup.append([csv_list[num][0], csv_list[num][1]])
    if printable:
        print "Noti Saver-------------------"
        for items in dup:
            for col in items:
                print col, "|",
            print
    return dup


def dupllicate_tuple_logger(csv_list, printable=False):
    dup = []
    for num in range(1, len(csv_list)):
        if(not(csv_list[num][2] in dup)):
            dup.append(csv_list[num][2])
    if printable:
        print "Event Logger-------------------"
        for item in dup:
            print item
    return dup


def dupllicate_tuple_pro(csv_list, printable=False):
    dup = []
    for num in range(2, len(csv_list)):
        if(not(csv_list[num][1] in dup)):
            dup.append(csv_list[num][1])
    if printable:
        print "Noti Pro-------------------"
        for item in dup:
            print item
    return dup