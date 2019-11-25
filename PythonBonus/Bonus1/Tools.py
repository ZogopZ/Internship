import datetime


def get_working_dates(work_start, work_end):
    working_dates = []
    holidays = [datetime.date(2019, 12, 25),
                datetime.date(2020, 3, 25),
                datetime.date(2020, 4, 13),
                datetime.date(2020, 5, 1),
                ]

    date_generated = [work_start + datetime.timedelta(days=x) for x in range(0, (work_end - work_start).days)]

    for date in date_generated:
        if date.weekday() in (5, 6) or date.date() in holidays:
            continue
        working_dates.append(date)
    return working_dates


def time_left(so_many_today):
    tfl = []
    days_left = so_many_today.days                   ##################################################################
    seconds_left = so_many_today.seconds             # Generate specified values, according to calculated difference. #
    micro_seconds_left = so_many_today.microseconds  ##################################################################

    years_left = days_left // 365                   #########################################################
    days_left -= years_left * 365                   #                                                       #
    months_left = days_left // 30                   #                                                       #
    days_left -= months_left * 30                   #                                                       #
    weeks_left = days_left // 7                     #                                                       #
    days_left -= weeks_left * 7                     #   Generate specified time periods with simple math    #
    hours_left = seconds_left // 60 // 60           #                                                       #
    seconds_left -= 60 * 60 * hours_left            #                                                       #
    minutes_left = seconds_left // 60               #                                                       #
    seconds_left -= 60 * minutes_left               #                                                       #
    mil_seconds_left = micro_seconds_left // 1000   #                                                       #
    micro_seconds_left -= 1000 * mil_seconds_left   #########################################################
    tfl.extend([years_left, months_left, weeks_left, days_left,
                hours_left, minutes_left, seconds_left, mil_seconds_left, micro_seconds_left])
    # Add above time values to tfl list.

    return tfl
