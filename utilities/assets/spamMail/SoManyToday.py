# Calculates time left until date 13/05/2020 and time 17:00 EET UTC/GMT +2 hours.
# Also calculates how much money earned today and how much money earned since the start of the internship.

from datetime import timedelta

from Tools import *
# from Internship.PythonBonus.Bonus1.Tools import *
# Change above line with: from Tools import *
# if you want to run it one line from a terminal.

now = datetime.datetime.today()  # Get current date-time.

work_start = datetime.datetime(now.year, now.month, now.day, 9, 0, 0, 0)  # Datetime that work starts.
work_end = datetime.datetime(now.year, now.month, now.day, 17, 0, 0, 0)  # Datetime that work ends.

first_day_date = datetime.datetime(2019, 11, 13, 9)  # Specify starting date of internship.
last_day_date = datetime.datetime(2020, 5, 13, 9)  # Specify ending date of internship.

set_dates(first_day_date, last_day_date)  # Sets working dates, weekends
set_holidays()  # and holidays.
set_working_status(now)  # Sets working_status True if working, false if not.

total_to_be_paid = 580.8 * 6  # Total pay for 6 month internship.
pay_per_hour_8 = 23.232 / 8
pay_per_microsecond_8 = 23.232 / (8 * 60 * 60 * 1000 * 1000)   # Calculate pay per microsecond working 8 hours a day.
# Above pay_per_* values are pre calculated by the corresponding company as 23.232 euro per day.

so_many_today = last_day_date + timedelta(hours=8) - now  # Generate date difference.
tfl = time_left(so_many_today)  # This function returns time left in multiple time types.
output_1 = "Η πρακτική μου τελειώνει σε " + str(tfl[0]) + " χρόνια " \
           + str(tfl[1]) + " μήνες " + str(tfl[2]) + " εβδομάδες " \
           + str(tfl[3]) + " ημέρες " + "\r\n" + 49 * " " \
           + str(tfl[3]) + " ώρες " + str(tfl[4]) + " λεπτά " \
           + str(tfl[5]) + " δευτερόλεπτα " + "\r\n" + 49 * " " \
           + str(tfl[6]) + " χιλιοστά του δευτερολέπτου και " \
           + str(tfl[7]) + " μικροδευτερόλεπτα.\r\n"


output_2 = ""
time_worked_today = 0
if get_working_status():  # If I am working right now, calculate pay earned today.
    time_worked_today = now - datetime.datetime(now.year, now.month, now.day, 9)  # Calculate working time today.
    microseconds_passed_today = time_worked_today.total_seconds() * (10 ** 6)  # Convert to microseconds.
    euro_made_today = (microseconds_passed_today * pay_per_microsecond_8)
    output_2 = "Σήμερα έχω ήδη βγάλει " + str(euro_made_today) + " ευρώ" + \
               " και έχω δουλέψει περίπου " + str(microseconds_passed_today / (10 ** 6) / 60 / 60) + " ώρες.\r\n"
elif not get_working_status():
    if now < work_start:
        time_worked_today = now - now
        output_2 = "\nΑυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. Σε λιγάκι πιάνουμε δουλειά...\r\n"
    elif now > work_end:
        time_worked_today = work_end - work_start
        output_2 = "\nΑυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. Σήμερα βγήκε το μεροκάματο των 23,232 ευρώ. \r\n"


time_worked = 0
days_worked = 0
for day in working_dates:  # For each working day, calculate the sum of working seconds.
    days_worked += 1  # Calculate days worked for printing only.
    if day.year == now.year and day.month == now.month and day.day == now.day:
        break  # For today working seconds are already calculated.
    time_worked += 8 * 60 * 60
# hibernate_seconds = 2.48 * 8 * 60 * 60   # Total seconds worked, on non working days. (UNKNOWN REASON YET)
# time_worked += time_worked_today.total_seconds() + hibernate_seconds
time_worked += time_worked_today.total_seconds()


microseconds_passed = time_worked * (10 ** 6)  # Convert to microseconds.
microseconds_passed_off_days = paid_days_off(now) * 8 * 60 * 60 * (10 ** 6)
euro_made = (microseconds_passed + microseconds_passed_off_days) * pay_per_microsecond_8
monthly_wage_earned = 0
if (euro_made / 580.8) < 1:  # First month work was less than a full months work.
    monthly_wage_earned = euro_made - 359.63
elif (euro_made / 580.8) > 1:  # Not first month of work.
    full_months_passed = int((euro_made - 359.63) / 580.8)  # Calculate full months passed.
    monthly_wage_earned = euro_made - 359.63 - full_months_passed * 580.8
elif (euro_made / 580.8) == 1:  # Exactly one month's work.
    monthly_wage_earned = 580.8
output_3 = "Μηνιαία έχω βγάλει " + str(monthly_wage_earned) + \
           " ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι 2-5 μέρες που πληρώνομαι " \
           "κάθε μήνα χωρίς να δουλεύω...)\r\n"
output_4 = "Συνολικά έχω βγάλει " + str(euro_made) + " ευρώ και έχω δουλέψει " + \
           str(days_worked) + " ημέρες, συνυπολογίζοντας την σημερινή.\r\n\r\n"
signature = "Regards,\r\nZois Zogopoulos\r\n"
pySignature = 113 * " " + "This is an automated email from Python.\r\n"

dateString = "Ημερομηνία: " + str(now.date()) + "\r\nΏρα: " + str(now.time()) + "\r\n\r\n"
zois_email = dateString + output_1 + output_2 + output_3 + output_4 + signature + pySignature

print(zois_email)
send_email(zois_email)

