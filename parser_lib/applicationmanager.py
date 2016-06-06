# -*- coding: utf-8 -*-

import codecs
from parser_lib import table_manager

def convert_eventlogger(name):
    for n in eventlogger_table():
        if name in n:
            return n
    return ""


def eventlogger_table():
    table = []
    table.append("Screen Turned On")
    table.append("Screen Turned Off")
    table.append("Screen Unlocked")
    return table


def convert_package2name(name):
    name = name.replace(" ", "")
    for row in replace_table():
        if name in row[1]:
            return row[0]
    return name


def replace_table():
    table = []
    table.append(["카카오톡","com.kakao.talk"])
    table.append(["카카오페이지","com.kakao.page"])
    table.append(["아이러브파스타","com.patigames.ilovepasta4kakao"])
    table.append(["클래시 로얄","com.supercell.clashroyale"])
    table.append(["메시지","com.android.mms"])
    return table

# ------------
# white list
# ------------
def contains_whitelist(value) :
    for item in whitelist_name():
        if item == value:
            return True
        
    return False

def whitelist_name():
    whitelist = []
    whitelist.append("카카오톡")
    whitelist.append("카카오페이지")
    whitelist.append("아이러브파스타")
    whitelist.append("메시지")
    whitelist.append("S헬스")
    whitelist.append("전화")
    whitelist.append("클래시 로얄")
    whitelist.append("알람/시간")
    whitelist.append("Facebook")
    whitelist.append("Instagram")
    whitelist.append("모두의마블")
    whitelist.append("지니 뮤직")
    whitelist.append("Slack")
    whitelist.append("Gmail")
    whitelist.append("케이웨더 날씨")
    whitelist.append("쿠차")
    whitelist.append("CLiP")
    whitelist.append("캘린더")
    whitelist.append("스프레드시트")
    whitelist.append("4shared")
    whitelist.append("전자출결")
    whitelist.append("캘린더")
    whitelist.append("kt 패밀리박스")
    return whitelist

###
# black list
# ------------

def contains_blacklist_package(name):
    for i in black_list_package():
        if name == i:
            return True
    return False


def contains_blacklist_name(name):
    for i in black_list_name():
        if name == i:
            return True
    return False


def contains_filter(name):
    return contains_blacklist_name(name) or contains_blacklist_package(name)


def black_list_name():
    f_list = []
    f_list.append("버즈런처")
    f_list.append("시스템 UI")
    f_list.append("안드로이드 시스템")
    f_list.append("라디오팟")
    f_list.append("올레 고객센터")
    f_list.append("KTPackageInstalller")
    f_list.append("AZ Screen Recorder")
    f_list.append("올레 WiFi접속")
    f_list.append("NH뱅킹")
    f_list.append("Galaxy Apps")
    f_list.append("AhnLab V3 Mobile Plus 2.0")
    return f_list


def black_list_package():
    f_list = []
    f_list.append("com.buzzpia.aqua.launcher")
    f_list.append("com.android.systemui")
    f_list.append("android")
    f_list.append("com.freeapp.androidapp")
    f_list.append("com.ktshow.cs")
    f_list.append("com.kt.om.ktpackageinstaller")
    f_list.append("com.hecorat.screenrecorder.free")
    f_list.append("com.kt.wificm")
    f_list.append("nh.smart")
    f_list.append("com.sec.android.app.samsungapps")
    f_list.append("com.ahnlab.v3mobileplus")
    return f_list


def getDefaultAppInfo(appusage, event_logger, saver, export_path, printable=False):
    with codecs.open(export_path, 'w', encoding="utf8") as csvfile:

        l = table_manager.dupllicate_tuple_app_usage(appusage, printable)
        # table_manager.dupllicate_tuple_logger(event_logger, True)
        csvfile.write('App usage-------------------\n')
        for row in l:
            csvfile.write(row.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ")+'\n')

        if printable:
            print
        l = table_manager.dupllicate_tuple_saver(saver, printable)
        csvfile.write('Noti Saver-------------------\n')
        for row in l:
            for col in row:
                csvfile.write(col.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ")+'\n')

        if printable:
            print
            print "black list by app name ---------------"
        csvfile.write("black list by app name ---------------\n")
        for i in black_list_name():
            if printable:
                print i
            csvfile.write(i.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ")+'\n')

        if printable:
            print
            print "black list by package name ---------------"
        csvfile.write("black list by package name ---------------\n")
        for i in black_list_package():
            if printable:
                print i
            csvfile.write(i.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ")+'\n')

        if printable:
            print
            print "white list by app name ---------------"
        csvfile.write("white list by app name ---------------\n")
        for i in whitelist_name():

            if printable:
                print i
            csvfile.write(i.decode("utf-8").replace(",", "，".decode("utf-8")).replace("\n", " ")+'\n')