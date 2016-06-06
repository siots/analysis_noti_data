#-*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time


def format_time_app_usage(times):
    times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    format_times = datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    return format_times


def format_time_event_logger(times):
    times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    format_times = datetime.strptime(times, '%Y. %m. %d. %p %I:%M:%S')
    return format_times


def format_time_hn(times):
    times = times.encode("utf-8").replace("오전", "AM").replace("오후","PM")
    format_times = datetime.strptime(times, ' %Y-%m-%d %H:%M:%S')
    return format_times


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