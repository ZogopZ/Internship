# Calculates time left until date 13/05/2020 and time 17:00 EET UTC/GMT +2 hours.

import datetime

now = datetime.datetime.today()       # Get current date-time.
first_day = datetime.datetime(2019, 11, 13, 0, 0, 0)    # Specify start date-time of internship.
last_day = datetime.datetime(2020, 5, 13, 17, 0, 0, 0)  # Specify ending date-time of internship.
start_time_day = datetime.datetime(now.year, now.month, now.day, 9, 0, 0, 0)    # Specify start date-time of each day.

total_to_be_paid = (580.8 - 580.8*0.2976)*6     # Total pay for 6 month internship.
pay_per_microsecond_8 = total_to_be_paid / (122 * 8 * 60 * 60 * 1000 * 1000)

so_many_today = last_day - now    # Generate date difference.

days_left = so_many_today.days                   ##################################################################
seconds_left = so_many_today.seconds             # Generate specified values, according to calculated difference. #
micro_seconds_left = so_many_today.microseconds  ##################################################################

years_left = days_left // 365                    #########################################################
days_left -= years_left * 365                    #                                                       #
months_left = days_left // 30                    #   Generate specified time periods with simple math    #
days_left -= months_left * 30                    #                                                       #
weeks_left = days_left // 7                      #                                                       #
days_left -= weeks_left * 7                      #                                                       #
hours_left = seconds_left // 60 // 60            #                                                       #
seconds_left -= 60*60*hours_left                 #                                                       #
minutes_left = seconds_left // 60                #                                                       #
seconds_left -= 60*minutes_left                  #                                                       #
mil_seconds_left = micro_seconds_left // 1000    #                                                       #
micro_seconds_left -= 1000 * mil_seconds_left    #########################################################

print("\nΗ πρακτική τελειώνει σε " + str(years_left) + " χρόνια "
      + str(months_left) + " μήνες " + str(weeks_left) + " εβδομάδες "
      + str(days_left) + " ημέρες " + str(hours_left) + " ώρες "
      + str(minutes_left) + " λεπτά " + str(seconds_left) + " δευτερόλεπτα "
      + str(mil_seconds_left) + " χιλιοστά του δευτερολέπτου και "
      + str(micro_seconds_left) + " μικροδευτερόλεπτα.")


time_passed_today = now - start_time_day    # Calculate working time today.
microseconds_passed_today = time_passed_today.total_seconds() * (10**6)     # Convert to microseconds.
euro_made_today = (microseconds_passed_today * pay_per_microsecond_8)

print("\nΣήμερα έχω ήδη βγάλει " + str(euro_made_today) + " ευρώ.")

time_passed = now - first_day   # Calculate sum of working time, since the beginning of the internship.
microseconds_passed = time_passed.total_seconds()*(10**6)   # Convert to microseconds.
pay_per_microsecond_24 = total_to_be_paid / ((last_day - first_day).total_seconds() * (10**6))
# This is not the true pay per microsecond. It is calculated using a time period equal to 24 hours per day, instead of
# 8 hours per day.
euro_made = (microseconds_passed * pay_per_microsecond_24)

print("Συνολικά έχω βγάλει " + str(euro_made) + ".")


def get_working_dates():
    working_dates = []
    work_start = datetime.datetime(2019, 11, 13, 9, 0, 0)
    work_end = datetime.datetime(2020, 5, 13, 17, 0, 0)
    holidays = [datetime.date(2019, 12, 25),
                datetime.date(2019, 12, 26),
                datetime.date(2020, 1, 1),
                datetime.date(2020, 1, 6),
                datetime.date(2020, 3, 2),
                datetime.date(2020, 3, 25),
                datetime.date(2020, 4, 17),
                datetime.date(2020, 4, 18),
                datetime.date(2020, 4, 19),
                datetime.date(2020, 4, 20),
                datetime.date(2020, 5, 1),
                ]

    date_generated = [work_start + datetime.timedelta(days=x) for x in range(0, (work_end - work_start).days)]

    for date in date_generated:
        if date.weekday() in (5, 6) or date.date() in holidays:
            continue
        working_dates.append(date)
    return working_dates
