# Calculates time left until date 13/05/2020 and time 17:00 EET UTC/GMT +2 hours.
# Also calculates how much money earned today and how much money earned since the start of the internship.

import datetime
from datetime import timedelta
from PythonBonus.Bonus1.Tools import *

now = datetime.datetime.today()       # Get current date-time.
first_day_date = datetime.datetime(2019, 11, 13, 9)     # Specify starting date of internship.
last_day_date = datetime.datetime(2020, 5, 13, 9)       # Specify ending date of internship.
set_dates(first_day_date, last_day_date)                # Sets working dates, weekends
set_holidays()                                          # and holidays.
set_working_status(now)                                 # Sets working_status True if working, false if not.

total_to_be_paid = (580.8 - 580.8*0.2976)*6     # Total pay for 6 month internship.
pay_per_microsecond_8 = total_to_be_paid / (len(working_dates) * 8 * 60 * 60 * 1000 * 1000)
# Calculate pay per microsecond working 8 hours a day.

so_many_today = last_day_date + timedelta(hours=8) - now    # Generate date difference.
tfl = time_left(so_many_today)  # This function returns time left in multiple time types.
print("\nΗ πρακτική μου τελειώνει σε " + str(tfl[0]) + " χρόνια "
      + str(tfl[1]) + " μήνες " + str(tfl[2]) + " εβδομάδες "
      + str(tfl[3]) + " ημέρες " + str(tfl[3]) + " ώρες "
      + str(tfl[4]) + " λεπτά " + str(tfl[5]) + " δευτερόλεπτα "
      + str(tfl[6]) + " χιλιοστά του δευτερολέπτου και "
      + str(tfl[7]) + " μικροδευτερόλεπτα.")

if get_working_status():    # If I am working right now, calculate pay earned today.
    time_worked_today = now - datetime.datetime(now.year, now.month, now.day, 9)    # Calculate working time today.
    microseconds_passed_today = time_worked_today.total_seconds() * (10 ** 6)     # Convert to microseconds.
    euro_made_today = (microseconds_passed_today * pay_per_microsecond_8)
    print("\nΣήμερα έχω ήδη βγάλει " + str(euro_made_today) + " ευρώ.")
elif not get_working_status():
    print("\nΣήμερα δεν δουλεύω...Ουχουυυυυυυυυ.")


time_worked = 0
for day in working_dates:  # For each working day, calculate the sum of working seconds.
    if day.year == now.year and day.month == now.month and day.day == now.day:
        break   # For today working seconds are already calculated.
    time_worked += 8*60*60
if get_working_status():    # If I am working right now, add pay earned today to total pay until previous pay day.
    time_worked += time_worked_today.total_seconds()    # Add working seconds for today.
elif not get_working_status() and now.date in working_dates:    # If I am not working right now, but I will or I was,
    time_worked += time_worked_today                            # add pay earned today to total pay.
microseconds_passed = time_worked*(10**6)   # Convert to microseconds.
euro_made = (microseconds_passed * pay_per_microsecond_8)
print("Συνολικά έχω βγάλει " + str(euro_made) + " ευρώ.")
