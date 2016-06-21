#-*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
from dateutil.parser import *


def format_time_parser(times):
    date = times.encode("utf-8").replace("오전", "AM").replace("오후","PM").replace("월","")
    try:
        format_times = parse(date)
    except ValueError:
        formats = ['%Y-%m-%d %H:%M:%S', '%Y. %m. %d. %p %I:%M:%S', '%b %d, %Y %I:%M:%S %p']
        for format in formats:
            try:
                format_times = datetime.strptime(date, format)
                return format_times
            except ValueError:
                pass

    return format_times

def format_time_app_usage(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    # return format_times
    return format_time_parser(times)

def format_time_app_usage_eu(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, '%m-%d-%Y %H:%M:%S')
    # return format_times
    return format_time_parser(times)


def format_time_event_logger(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, '%Y. %m. %d. %p %I:%M:%S')
    # return format_times
    return format_time_parser(times)

def format_time_event_logger_eu(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, '%b %d, %Y %I:%M:%S %p')
    # return format_times
    return format_time_parser(times)


def format_time_hn(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, ' %Y-%m-%d %H:%M:%S')
    # return format_times
    return format_time_parser(times)

def format_time_another(times):
    # times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    # format_times = datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    # return format_times
    return format_time_parser(times)

def formatdate_to_sec(format_times):
    secs = time.mktime(format_times.timetuple())
    return secs


def start_end_days(datetimes):

    format_times = datetime.strptime(datetimes, '%Y-%m-%d')
    start = formatdate_to_sec(format_times)
    return start, start + 86400


def contains_day(secondsofday, datetimes):
    if datetimes is None:
        return False
    start, end = start_end_days(datetimes)
    return secondsofday >= start and secondsofday <= end


if __name__ == "__main__":
    print format_time_parser("2016. 6. 21. AM 11:21:12")