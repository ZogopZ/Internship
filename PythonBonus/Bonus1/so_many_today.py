# Calculates time left until date 13/05/2020 and time 17:00 EET UTC/GMT +2 hours.

import datetime

today = datetime.datetime.today()       # Get current date.
last_day = datetime.datetime(2020, 5, 13, 17, 0, 0, 0)  # Specify ending date.

so_many_today = last_day - today    # Generate date difference.

days_left = so_many_today.days                   ##################################################################
seconds_left = so_many_today.seconds             # Generate specified values, according to calculated difference. #
micro_seconds_left = so_many_today.microseconds  ##################################################################

years_left = days_left // 365                   #########################################################
days_left -= years_left * 365                   #                                                       #
months_left = days_left // 30                   #   Generate specified time periods with simple math    #
days_left -= months_left * 30                   #                                                       #
weeks_left = days_left // 7                     #                                                       #
days_left -= weeks_left * 7                     #                                                       #
hours_left = seconds_left // 60 // 60           #                                                       #
seconds_left -= 60*60*hours_left                #                                                       #
minutes_left = seconds_left // 60               #                                                       #
seconds_left -= 60*minutes_left                 #                                                       #
mil_seconds_left = micro_seconds_left // 1000   #                                                       #
micro_seconds_left -= 1000 * mil_seconds_left   #########################################################

print("Η πρακτική τελειώνει σε " + str(years_left) + " χρόνια "
      + str(months_left) + " μήνες " + str(weeks_left) + " εβδομάδες "
      + str(days_left) + " ημέρες " + str(hours_left) + " ώρες "
      + str(minutes_left) + " λεπτά " + str(seconds_left) + " δευτερόλεπτα "
      + str(mil_seconds_left) + " χιλιοστά του δευτερολέπτου και "
      + str(micro_seconds_left) + " μικροδευτερόλεπτα.")

